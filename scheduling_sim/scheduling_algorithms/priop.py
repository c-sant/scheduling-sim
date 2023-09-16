from scheduling_sim.scheduling_algorithms.prioc import PriorityCooperativeScheduler


class PriorityPreemptiveScheduler(PriorityCooperativeScheduler):
    algorithm_name: str = "Priority Preemptive Scheduler"

    def has_higher_priority_process_waiting(self) -> bool:
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
