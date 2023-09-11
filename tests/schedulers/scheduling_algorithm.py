import pytest

from scheduling_sim import Process, SchedulingAlgorithm


class TestSchedulingAlgorithm:
    n_of_test_cases = 3
    test_cases = list(range(n_of_test_cases))
    test_cases_ids = [f"Case {i + 1}" for i in test_cases]

    Scheduler = SchedulingAlgorithm

    # results
    average_wait_times = [0] * n_of_test_cases
    average_turnaround_times = [0] * n_of_test_cases
    total_execution_times = [0] * n_of_test_cases

    # cases

    def case_1(self) -> Scheduler:
        processes = [
            Process("P1", arrival_time=0, execution_time=5, priority_level=2),
            Process("P2", arrival_time=0, execution_time=2, priority_level=3),
            Process("P3", arrival_time=1, execution_time=4, priority_level=1),
            Process("P4", arrival_time=3, execution_time=1, priority_level=4),
            Process("P5", arrival_time=5, execution_time=2, priority_level=5),
        ]

        return self.Scheduler(processes)

    def case_2(self) -> Scheduler:
        processes = [
            Process("P1", arrival_time=0, execution_time=5, priority_level=3),
            Process("P2", arrival_time=2, execution_time=4, priority_level=2),
            Process("P3", arrival_time=2, execution_time=3, priority_level=1),
            Process("P4", arrival_time=4, execution_time=4, priority_level=4),
            Process("P5", arrival_time=4, execution_time=1, priority_level=5),
        ]

        return self.Scheduler(processes)

    def case_3(self) -> Scheduler:
        processes = [
            Process("P1", arrival_time=0, execution_time=5, priority_level=3),
            Process("P2", arrival_time=1, execution_time=2, priority_level=2),
            Process("P3", arrival_time=2, execution_time=4, priority_level=1),
            Process("P4", arrival_time=3, execution_time=3, priority_level=4),
            Process("P5", arrival_time=5, execution_time=2, priority_level=5),
        ]

        return self.Scheduler(processes)

    def get_scheduler(self, case_id: int) -> Scheduler:
        cases = [self.case_1, self.case_2, self.case_3]

        return cases[case_id]()

    parametrize_test = pytest.mark.parametrize(
        "case_id", test_cases, ids=test_cases_ids
    )

    @parametrize_test
    def test_average_wait_time(self, case_id: int):
        scheduler = self.get_scheduler(case_id)
        expected_avg_wait_time = self.average_wait_times[case_id]

        assert scheduler.average_wait_time == expected_avg_wait_time

    @parametrize_test
    def test_average_turnaround_time(self, case_id: int):
        scheduler = self.get_scheduler(case_id)
        expected_avg_turnaround_time = self.average_turnaround_times[case_id]

        assert scheduler.average_turnaround_time == expected_avg_turnaround_time

    @parametrize_test
    def test_total_execution_time(self, case_id: int):
        scheduler = self.get_scheduler(case_id)
        expected_total_execution_time = self.total_execution_times[case_id]

        assert scheduler.total_execution_time == expected_total_execution_time
