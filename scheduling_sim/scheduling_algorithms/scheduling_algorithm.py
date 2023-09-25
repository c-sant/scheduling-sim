import pandas as pd

from scheduling_sim.exceptions import (
    InvalidProcessQueueError,
    NoProcessesInQueueError,
    NoProcessWithArrivalTimeZeroError,
)
from scheduling_sim.process import Process


class SchedulingAlgorithm:
    """Represents a generic scheduling algorithm for managing a list of processes.

    This class serves as a template for implementing specific scheduling algorithms.
    It provides basic functionality for managing processes and ensuring the validity
    of process queues.

    Attributes:
        algorithm_name (str): The name of the scheduling algorithm.
        number_of_processes (int): The number of processes in the scheduling algorithm.
        total_execution_time (int): The total execution time of all processes.

    Methods:
        reset(): Resets the scheduling algorithm and processes to their initial
        states.
        add_process(process: Process): Adds a process to the scheduling algorithm.
        run() -> pd.DataFrame: Executes the scheduling algorithm.

    Properties:
        number_of_processes (int): The number of processes in the scheduling algorithm.
        total_execution_time (int): The total execution time of all processes.
        average_turnaround_time (float): The average turnaround time of all processes.
        average_wait_time (float): The average wait time of all processes.
        ready_queue_is_empty (bool): Whether or not the ready queue has no Process
        objects.
        is_executing_a_process (bool): Whether or not there is a process running
        at the moment.
    """

    _processes: list[Process] = []
    _ready_queue: list[Process] = []
    _current_running_process: Process = None

    algorithm_name: str = "Scheduling Algorithm"

    def __init__(self, processes: list[Process] = None):
        self._processes: list[Process] = []

        if processes != None:
            for process in processes:
                self.add_process(process)

        self.reset()
        self._assert_queue_validity()

    def __repr__(self):
        return f"{self.algorithm_name} (Processes: {self.number_of_processes})"

    @property
    def number_of_processes(self) -> int:
        """int: The number of processes in the scheduling algorithm."""

        return len(self._processes)

    @property
    def total_execution_time(self) -> int:
        """int: The total execution time of all processes."""

        if len(self._processes) == 0:
            return 0

        return sum([process.execution_time for process in self._processes])

    @property
    def average_turnaround_time(self) -> int:
        """int: The average turnaround time of all processes."""
        self.run()

        total_turnaround_time = sum(
            [process.turnaround_time for process in self._processes]
        )

        return total_turnaround_time / len(self._processes)

    @property
    def average_wait_time(self) -> int:
        """int: The average wait time of all processes."""
        self.run()

        total_wait_time = sum([process.wait_time for process in self._processes])

        return total_wait_time / len(self._processes)

    @property
    def ready_queue_is_empty(self) -> bool:
        """bool: Whether or not the ready queue has no Process objects."""
        return len(self._ready_queue) == 0

    @property
    def is_executing_a_process(self) -> bool:
        """bool: Whether or not there is a process running at the moment."""
        return (
            self._current_running_process != None
            and self._current_running_process.is_running
        )

    def reset(self):
        """Resets the scheduling algorithm and processes to their initial states."""

        for process in self._processes:
            process.reset()

        self._current_running_process = None
        self._ready_queue: list[Process] = []

    def add_process(self, process: Process):
        """Adds a process to the scheduling algorithm.

        Args:
            process (Process): The process to be added.

        Raises:
            InvalidProcessQueueError: If the provided process is not of type Process.
        """

        if type(process) != Process:
            raise InvalidProcessQueueError()

        self._processes.append(process)

    def run(self) -> pd.DataFrame:
        """Executes the scheduling algorithm."""

        self.reset()
        execution_report = pd.DataFrame()

        for step in range(self.total_execution_time + 1):
            self._simulate_scheduling_step(step)
            step_report = self._report_step_status(step)

            execution_report = pd.concat(
                [execution_report, step_report], ignore_index=True
            )

        return execution_report

    def _simulate_scheduling_step(self, step: int):
        """Executes a step of the schedule.

        Args:
            step (int): The executed step.
        """

        self._update_processes_statuses(step)
        self._refresh_ready_queue()
        self._determine_current_running_process()

    def _report_step_status(self, step: int) -> pd.DataFrame:
        """Reports the status of processes at the current step.

        Args:
            step (int): The current step.

        Returns:
            pd.DataFrame: A DataFrame containing the step's process status report.
        """

        step_report = pd.DataFrame()

        for process in self._processes:
            process_report = pd.DataFrame(
                {
                    "time": [step],
                    "process_name": [process.name],
                    "process_status": [process.status.value],
                    "remaining_execution_time": [process.remaining_execution_time],
                    "quantum_progress": [process.quantum_progress],
                }
            )

            step_report = pd.concat([step_report, process_report], ignore_index=True)

        return step_report

    def _assert_queue_validity(self):
        """Validates the integrity of process queues.

        Raises:
            InvalidProcessQueueError: If the process queue is not a list of Process
            objects.
            NoProcessesInQueueError: If the process queue is empty.
            NoProcessWithArrivalTimeZeroError: If none of the processes have an
            arrival time of zero.
        """

        # if the process queue is not a list of Process objects
        if type(self._processes) != list:
            raise InvalidProcessQueueError()

        # if the process queue is empty
        if len(self._processes) == 0:
            raise NoProcessesInQueueError()

        some_process_arrives_at_zero = False
        for process in self._processes:
            # if any object in the process queue is not a Process
            if type(process) != Process:
                raise InvalidProcessQueueError()

            if process.arrival_time == 0:
                some_process_arrives_at_zero = True

        # if no process have an arrival time of zero
        if not some_process_arrives_at_zero:
            raise NoProcessWithArrivalTimeZeroError()

    def _update_processes_statuses(self, time: int):
        """Updates the statuses of processes based on the current time.

        This method updates the statuses of processes in the scheduling algorithm
        based on their arrival times and remaining execution times. It handles
        transitions between READY, WAITING, RUNNING, INTERRUPTED and TERMINATED
        states.

        Args:
            time (int): The current time.
        """

        # if there is a Process object currently running
        if self.is_executing_a_process:
            self._current_running_process.remaining_execution_time -= 1

        for process in self._processes:
            # if Process has been interrupted or is ready and arrives, it starts
            # to wait
            if process.was_interrupted or (
                process.is_ready and process.arrival_time == time
            ):
                process.wait()
                process.enqueue_time = time

            # if the current running Process has no remaining execution time, it
            # terminates
            if process.is_running and process.remaining_execution_time == 0:
                process.conclude()
                process.conclusion_time = time

    def _determine_current_running_process(self):
        """Determines the currently running process from the ready queue.

        When the current running process is terminated or non existent, this method
        selects the next process to run from the ready queue (if there are any).
        """

        if (not self.is_executing_a_process) and (not self.ready_queue_is_empty):
            self._current_running_process = self._ready_queue.pop(0)
            self._current_running_process.run()

    def _refresh_ready_queue(self):
        """Refresh the ready queue based on waiting processes.

        This method updates the ready queue by selecting processes with WAITING
        status from the list of all processes in the scheduling algorithm.
        """

        self._ready_queue: list[Process] = [
            process for process in self._processes if process.is_waiting
        ]

        self._ready_queue = sorted(self._ready_queue, key=lambda x: x.enqueue_time)
