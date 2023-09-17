from scheduling_sim.scheduling_algorithms.prioc import PriorityCooperativeScheduler


class PriorityPreemptiveScheduler(PriorityCooperativeScheduler):
    """Priority Preemptive Scheduler

    This class represents a scheduling algorithm that schedules processes
    based on their priority levels with preemption. Higher-priority processes
    can preempt lower-priority ones if they become available.

    Attributes:
        algorithm_name (str): The name of the scheduling algorithm.

    Methods:
        reset(): Resets the scheduling algorithm and processes to their initial
        states.
        add_process(process: Process): Adds a process to the scheduling algorithm.
        run() -> pd.DataFrame: Executes the scheduling algorithm.
        has_higher_priority_process_waiting() -> bool: Checks if a higher-priority
        process is waiting to execute.

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

    algorithm_name: str = "Priority Preemptive Scheduler"

    def has_higher_priority_process_waiting(self) -> bool:
        """Checks if a higher-priority process is waiting to execute.

        Returns:
            bool: True if there is a higher-priority process in the ready queue;
            False otherwise.
        """

        if (not self.is_executing_a_process) or self.ready_queue_is_empty:
            return False

        most_prioritary_waiting_process = self._ready_queue[0]

        if self.use_reverse_priority:
            return (
                self._current_running_process.priority_level
                < most_prioritary_waiting_process.priority_level
            )
        else:
            return (
                self._current_running_process.priority_level
                > most_prioritary_waiting_process.priority_level
            )

    def _determine_current_running_process(self):
        if (
            self.is_executing_a_process
            and (not self.ready_queue_is_empty)
            and self.has_higher_priority_process_waiting()
        ):
            self._current_running_process.interrupt()

        super()._determine_current_running_process()
