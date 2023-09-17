from scheduling_sim.scheduling_algorithms.sjf import ShortestJobFirstScheduler


class ShortestRemainingTimeFirstScheduler(ShortestJobFirstScheduler):
    """Shortest Remaining Time First Scheduler

    This class represents a scheduling algorithm that schedules processes
    based on their remaining execution time. The process with the shortest
    remaining execution time is given priority and executed first, making
    it a preemptive scheduling algorithm.

    Attributes:
        algorithm_name (str): The name of the scheduling algorithm.

    Methods:
        reset(): Resets the scheduling algorithm and processes to their initial
        states.
        add_process(process: Process): Adds a process to the scheduling algorithm.
        run() -> pd.DataFrame: Executes the scheduling algorithm.
        has_shorter_process_waiting() -> bool: Checks if a process with shorter
        remaining execution time is waiting.

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

    algorithm_name: str = "Shortest Remaining Time First"

    def has_shorter_process_waiting(self) -> bool:
        """Checks if a process with shorter remaining execution time is waiting.

        Returns:
            bool: True if there is a process with shorter remaining execution time
            in the ready queue; False otherwise.
        """

        if (not self.is_executing_a_process) or self.ready_queue_is_empty:
            return False

        shortest_waiting_process = self._ready_queue[0]

        return (
            self._current_running_process.remaining_execution_time
            > shortest_waiting_process.remaining_execution_time
        )

    def _determine_current_running_process(self):
        if (
            self.is_executing_a_process
            and (not self.ready_queue_is_empty)
            and self.has_shorter_process_waiting()
        ):
            self._current_running_process.interrupt()

        super()._determine_current_running_process()
