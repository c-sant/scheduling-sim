from scheduling_sim.scheduling_algorithms.scheduling_algorithm import (
    SchedulingAlgorithm,
)


class FirstComeFirstServeScheduler(SchedulingAlgorithm):
    """First Come First Serve Scheduler

    This class represents a scheduling algorithm that executes processes in the
    order they arrive. Non-preemptive.

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
