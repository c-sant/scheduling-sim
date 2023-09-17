from scheduling_sim.process import Process
from scheduling_sim.scheduling_algorithms.scheduling_algorithm import (
    SchedulingAlgorithm,
)


class RoundRobinScheduler(SchedulingAlgorithm):
    """Round Robin Scheduler

    This class represents a scheduling algorithm that schedules processes
    in a circular manner, with each process receiving a fixed time slice
    called a quantum before being preempted and moved to the back of the queue.

    Attributes:
        algorithm_name (str): The name of the scheduling algorithm.

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
        quantum_length (int): The length of each time quantum.
    """

    algorithm_name: str = "Round Robin Scheduler"
    _quantum_length: int = 2

    def __init__(self, processes: list[Process] = None, quantum_length: int = 2):
        super().__init__(processes)
        self.quantum_length = quantum_length

    @property
    def quantum_length(self) -> int:
        """int: Length of each time quantum."""

        return self._quantum_length

    @quantum_length.setter
    def quantum_length(self, value: int):
        """Length of each time quantum.

        Args:
            value (int): The length of each time quantum.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 1.
        """

        if type(value) != int:
            raise TypeError(
                f"Quantum length should be an integer. Got {type(value)} instead."
            )

        if value < 1:
            raise ValueError(
                f"Quantum length should be higher than 0. Got {value} instead."
            )

        self._quantum_length = value

    def _simulate_scheduling_step(self, step: int):
        super()._simulate_scheduling_step(step)
        self._current_running_process.quantum_progress += 1

    def _determine_current_running_process(self):
        if (
            self.is_executing_a_process
            and self._current_running_process.quantum_progress == self.quantum_length
        ):
            self._current_running_process.quantum_progress = 0
            self._current_running_process.interrupt()

        super()._determine_current_running_process()
