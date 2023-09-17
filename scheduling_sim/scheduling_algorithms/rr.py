from scheduling_sim.process import Process
from scheduling_sim.scheduling_algorithms.scheduling_algorithm import (
    SchedulingAlgorithm,
)


class RoundRobinScheduler(SchedulingAlgorithm):
    algorithm_name: str = "Round Robin Scheduler"
    _quantum_length: int = 2

    def __init__(self, processes: list[Process] = None, quantum_length: int = 2):
        super().__init__(processes)
        self.quantum_length = quantum_length

    @property
    def quantum_length(self) -> int:
        return self._quantum_length

    @quantum_length.setter
    def quantum_length(self, value: int):
        if type(value) != int:
            raise TypeError(
                f"Quantum length should be an integer. Got {type(value)} instead."
            )

        if value < 1:
            raise ValueError(
                f"Quantum length should be higher than 0. Got {value} instead."
            )

        self._quantum_length = value

    def _simulate_scheduling_step(self, step: int):
        super()._simulate_scheduling_step(step)
        self._current_running_process.quantum_progress += 1

    def _determine_current_running_process(self):
        if (
            self.is_executing_a_process
            and self._current_running_process.quantum_progress == self.quantum_length
        ):
            self._current_running_process.quantum_progress = 0
            self._current_running_process.interrupt()

        super()._determine_current_running_process()
