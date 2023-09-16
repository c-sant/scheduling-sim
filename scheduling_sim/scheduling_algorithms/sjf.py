from scheduling_sim.scheduling_algorithms.scheduling_algorithm import (
    SchedulingAlgorithm,
)


class ShortestJobFirstScheduler(SchedulingAlgorithm):
    """Shortest Job First Scheduler

    This class represents a scheduling algorithm that schedules processes based
    on their execution time. Processes with the shortest execution time are given
    priority and executed first. Non-preemptive.

    Attributes:
        algorithm_name (str): The name of the scheduling algorithm.
    """

    algorithm_name: str = "Shortest Job First Scheduler"

    def _refresh_ready_queue(self):
        """Refresh the ready queue based on waiting processes.

        This method updates the ready queue by selecting processes with WAITING
        status from the list of all processes in the scheduling algorithm. The queue
        is ordered according to the remaining time.
        """

        super()._refresh_ready_queue()

        self._ready_queue = sorted(
            self._ready_queue, key=lambda x: x.remaining_execution_time
        )
