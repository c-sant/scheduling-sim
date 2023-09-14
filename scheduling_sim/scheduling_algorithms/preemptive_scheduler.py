from scheduling_sim.scheduling_algorithms.scheduling_algorithm import (
    SchedulingAlgorithm,
)


class PreemptiveScheduler(SchedulingAlgorithm):
    """
    Represents a preemptive scheduling algorithm for managing a list of processes.

    This class is a subclass of the SchedulingAlgorithm class and is designed to
    implement a preemptive scheduling algorithm. Preemptive scheduling allows the
    scheduler to interrupt the execution of a running process and switch to another
    process if a higher-priority process becomes available.

    Attributes:
        algorithm_name (str): The name of the preemptive scheduling algorithm.
    """

    algorithm_name: str = "Preemptive Scheduler"
    