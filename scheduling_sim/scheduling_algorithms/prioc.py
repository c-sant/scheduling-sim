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
    """

    _use_reverse_priority: bool = True
    algorithm_name: str = "First Come First Serve Scheduler"

    def __init__(
        self, processes: list[Process] = None, use_reverse_priority: bool = True
    ):
        super().__init__(processes)
        self.use_reverse_priority = use_reverse_priority

    @property
    def use_reverse_priority(self) -> bool:
        return self._use_reverse_priority

    @use_reverse_priority.setter
    def use_reverse_priority(self, value: bool):
        if type(value) != bool:
            raise ValueError(
                f"expected bool value for use_reverse_priority. Got {type(value).__name__} instead."
            )

        self._use_reverse_priority = value

    def _refresh_ready_queue(self):
        """Refresh the ready queue based on waiting processes.

        This method updates the ready queue by selecting processes with WAITING
        status from the list of all processes in the scheduling algorithm. The queue
        is ordered according to the arrival time.
        """

        super()._refresh_ready_queue()

        self._ready_queue = sorted(
            self._ready_queue,
            key=lambda x: x.priority_level,
            reverse=self.use_reverse_priority,
        )
