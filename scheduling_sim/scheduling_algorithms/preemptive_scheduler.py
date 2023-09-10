from scheduling_sim.scheduling_algorithms.scheduling_algorithm import (
    SchedulingAlgorithm,
)


class PreemptiveScheduler(SchedulingAlgorithm):
    algorithm_name = "Preemptive Scheduler"

    def _simulate_scheduling_step(self, step: int):
        self._update_processes_statuses(step)
        self._refresh_ready_queue()
        self._determine_running_process_status()
        self._determine_current_running_process()
