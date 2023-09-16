from scheduling_sim.scheduling_algorithms.scheduling_algorithm import (
    SchedulingAlgorithm,
)


class FirstComeFirstServeScheduler(SchedulingAlgorithm):
    """First Come First Serve Scheduler

    This class represents a scheduling algorithm that executes processes in the
    order they arrive. Non-preemptive.

    Attributes:
        algorithm_name (str): The name of the scheduling algorithm.
    """

    algorithm_name: str = "First Come First Serve Scheduler"

    def _refresh_ready_queue(self):
        """Refresh the ready queue based on waiting processes.

        This method updates the ready queue by selecting processes with WAITING
        status from the list of all processes in the scheduling algorithm. The queue
        is ordered according to the arrival time.
        """

        super()._refresh_ready_queue()

        self._ready_queue = sorted(self._ready_queue, key=lambda x: x.arrival_time)
