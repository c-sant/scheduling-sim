from scheduling_sim.scheduling_algorithms.scheduling_algorithm import (
    SchedulingAlgorithm,
)


class CooperativeScheduler(SchedulingAlgorithm):
    """Represents a cooperative (non-preemptive) scheduling algorithm for managing a list of processes.

    This class is a subclass of the SchedulingAlgorithm class and is designed to
    implement a cooperative (non-preemptive) scheduling algorithm. In cooperative
    scheduling, processes run to completion without interruption, and the scheduler
    relies on processes voluntarily yielding control of the CPU or entering a waiting
    state.

    Attributes:
        algorithm_name (str): The name of the cooperative scheduling algorithm.
    """

    algorithm_name: str = "Cooperative Scheduler"
