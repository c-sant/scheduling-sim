from scheduling_sim.scheduling_algorithms.sjf import ShortestJobFirstScheduler


class ShortestRemainingTimeFirstScheduler(ShortestJobFirstScheduler):
    algorithm_name: str = "Shortest Remaining Time First"

    def _determine_current_running_process(self):
        if (
            self.is_executing_a_process
            and (not self.ready_queue_is_empty)
            and self._ready_queue[0].remaining_execution_time
            < self._current_running_process.remaining_execution_time
        ):
            self._current_running_process.interrupt()

        super()._determine_current_running_process()
