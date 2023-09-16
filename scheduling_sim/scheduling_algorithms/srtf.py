from scheduling_sim.scheduling_algorithms.sjf import ShortestJobFirstScheduler


class ShortestRemainingTimeFirstScheduler(ShortestJobFirstScheduler):
    algorithm_name: str = "Shortest Remaining Time First"

    def has_shorter_process_waiting(self) -> bool:
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
