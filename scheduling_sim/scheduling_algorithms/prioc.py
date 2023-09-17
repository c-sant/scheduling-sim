from scheduling_sim.process import Process
from scheduling_sim.scheduling_algorithms.scheduling_algorithm import (
    SchedulingAlgorithm,
)


class PriorityCooperativeScheduler(SchedulingAlgorithm):
    """Priority Cooperative Scheduler

    This class represents a scheduling algorithm that executes processes in the
    order of their priority level. Non-preemptive.

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
        use_reverse_priority (bool): If True, higher priority levels indicate higher
        priority; otherwise, they indicate lower priority.
    """

    _use_reverse_priority: bool = True
    algorithm_name: str = "Priority Cooperative Scheduler"

    def __init__(
        self, processes: list[Process] = None, use_reverse_priority: bool = True
    ):
        super().__init__(processes)
        self.use_reverse_priority = use_reverse_priority

    @property
    def use_reverse_priority(self) -> bool:
        """bool: If higher levels should indicate higher priority or not."""

        return self._use_reverse_priority

    @use_reverse_priority.setter
    def use_reverse_priority(self, value: bool):
        """If higher levels should indicate higher priority or not.

        Args:
            value (bool): A boolean value to enable (True) or disable (False) the
            reverse priority mode.

        Raises:
            ValueError: If the provided value is not a boolean.
        """

        if type(value) != bool:
            raise ValueError(
                f"expected bool value for use_reverse_priority. Got {type(value).__name__} instead."
            )

        self._use_reverse_priority = value

    def _refresh_ready_queue(self):
        """Refresh the ready queue based on waiting processes.

        This method updates the ready queue by selecting processes with WAITING
        status from the list of all processes in the scheduling algorithm. The queue
        is ordered according to their priority level.
        """

        super()._refresh_ready_queue()

        self._ready_queue = sorted(
            self._ready_queue,
            key=lambda x: x.priority_level,
            reverse=self.use_reverse_priority,
        )
