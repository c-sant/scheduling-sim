import pandas as pd

from scheduling_sim.exceptions import (
    InvalidProcessQueueError,
    NoProcessesInQueueError,
    NoProcessWithArrivalTimeZeroError,
)
from scheduling_sim.process import Process, ProcessStatus


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
        reset(): Resets the scheduling algorithm and processes to their initial states.
        add_process(process: Process): Adds a process to the scheduling algorithm.
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
        """int: The total execution time of all processes"""

        if len(self._processes) == 0:
            return 0

        return sum([process.execution_time for process in self._processes])

    @property
    def average_turnaround_time(self) -> int:
        self.run()

        total_turnaround_time = sum(
            [process.turnaround_time for process in self._processes]
        )

        return total_turnaround_time / len(self._processes)

    @property
    def average_wait_time(self) -> int:
        self.run()

        total_wait_time = sum([process.wait_time for process in self._processes])

        return total_wait_time / len(self._processes)

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
        """Execute the scheduling algorithm."""

        self.reset()
        execution_report = pd.DataFrame()

        for step in range(self.total_execution_time + 1):
            self._simulate_scheduling_step(step)

            step_report = pd.DataFrame()

            for process in self._processes:
                process_report = pd.DataFrame(
                    {
                        "time": [step],
                        "process_name": [process.name],
                        "process_status": [process.status],
                        "arrival_time": [process.arrival_time],
                        "priority_level": [process.priority_level],
                        "execution_time": [process.execution_time],
                        "wait_time": [process.wait_time],
                        "remaining_execution_time": [process.remaining_execution_time],
                        "turnaround_time": [process.turnaround_time],
                    }
                )

                step_report = pd.concat(
                    [step_report, process_report], ignore_index=True
                )

            execution_report = pd.concat(
                [execution_report, step_report], ignore_index=True
            )

        return execution_report

    def _simulate_scheduling_step(self, step: int):
        """Execute a step of the schedule.

        This method is intended to be implemented in subclasses of the SchedulingAlgorithm
        class. It defines the core logic for scheduling processes using the specific
        scheduling algorithm. Subclasses should override this method to provide their
        implementation.

        Args:
            step (int): The executed step.

        Raises:
            NotImplementedError: This method must be implemented in subclasses.
        """

        raise NotImplementedError()

    def _assert_queue_validity(self):
        """Validates the integrity of process queues.

        Raises:
            InvalidProcessQueueError: If the process queue is not a list of Process
            objects.
            NoProcessesInQueueError: If the process queue is empty.
            NoProcessWithArrivalTimeZeroError: If none of the processes have an
            arrival time of zero.
        """

        if type(self._processes) != list:
            raise InvalidProcessQueueError()

        if len(self._processes) == 0:
            raise NoProcessesInQueueError()

        some_process_arrives_at_zero = False
        for process in self._processes:
            if type(process) != Process:
                raise InvalidProcessQueueError()

            if process.arrival_time == 0:
                some_process_arrives_at_zero = True

        if not some_process_arrives_at_zero:
            raise NoProcessWithArrivalTimeZeroError()

    def _update_processes_statuses(self, time: int):
        """Update the statuses of processes based on the current time.

        This method updates the statuses of processes in the scheduling algorithm
        based on their arrival times and remaining execution times. It handles transitions
        between READY, WAITING, RUNNING, and TERMINATED states.

        Args:
            time (int): The current time.
        """
        if self._current_running_process != None:
            self._current_running_process.remaining_execution_time -= 1

        for process in self._processes:
            if process.status == ProcessStatus.WAITING:
                process.wait_time += 1

            if process.status == ProcessStatus.READY and process.arrival_time == time:
                process.status = ProcessStatus.WAITING

            if (
                process.status == ProcessStatus.RUNNING
                and process.remaining_execution_time == 0
            ):
                process.status = ProcessStatus.TERMINATED

    def _determine_running_process_status(self):
        """Determine the status of the currently running process and handle termination.

        This method checks the status of the currently running process and handles
        its transition to the TERMINATED state if its remaining execution time reaches
        zero.
        """

        if self._current_running_process == None:
            return

        if self._current_running_process.status == ProcessStatus.TERMINATED:
            self._current_running_process = None

    def _determine_current_running_process(self):
        """Determine the currently running process from the ready queue.

        This method selects the next process to run from the ready queue if there
        is no running process and there are available processes in the ready queue.
        """

        if (self._current_running_process != None) or (
            self._current_running_process == None and len(self._ready_queue) == 0
        ):
            return

        self._current_running_process = self._ready_queue.pop(0)
        self._current_running_process.status = ProcessStatus.RUNNING

    def _refresh_ready_queue(self):
        """Refresh the ready queue based on waiting processes.

        This method updates the ready queue by selecting processes with WAITING
        status from the list of all processes in the scheduling algorithm.
        """

        self._ready_queue: list[Process] = [
            process
            for process in self._processes
            if process.status == ProcessStatus.WAITING
        ]
