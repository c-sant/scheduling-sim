import pytest

from scheduling_sim import FirstComeFirstServeScheduler, Process


@pytest.fixture
def case1() -> FirstComeFirstServeScheduler:
    processes = [
        Process("P1", arrival_time=0, execution_time=5, priority_level=3),
        Process("P2", arrival_time=0, execution_time=2, priority_level=2),
        Process("P3", arrival_time=1, execution_time=4, priority_level=1),
        Process("P4", arrival_time=3, execution_time=1, priority_level=4),
        Process("P5", arrival_time=5, execution_time=2, priority_level=5),
    ]

    return FirstComeFirstServeScheduler(processes)


@pytest.fixture
def case2() -> FirstComeFirstServeScheduler:
    processes = [
        Process("P1", arrival_time=0, execution_time=5, priority_level=3),
        Process("P2", arrival_time=2, execution_time=4, priority_level=2),
        Process("P3", arrival_time=2, execution_time=3, priority_level=1),
        Process("P4", arrival_time=4, execution_time=4, priority_level=4),
        Process("P5", arrival_time=4, execution_time=1, priority_level=5),
    ]

    return FirstComeFirstServeScheduler(processes)


@pytest.fixture
def case3() -> FirstComeFirstServeScheduler:
    processes = [
        Process("P1", arrival_time=0, execution_time=5, priority_level=3),
        Process("P2", arrival_time=1, execution_time=2, priority_level=2),
        Process("P3", arrival_time=2, execution_time=4, priority_level=1),
        Process("P4", arrival_time=3, execution_time=3, priority_level=4),
        Process("P5", arrival_time=5, execution_time=2, priority_level=5),
    ]

    return FirstComeFirstServeScheduler(processes)


def test_fcfs_case_1_average_turnaround_time(case1: FirstComeFirstServeScheduler):
    assert (
        case1.average_turnaround_time == 8.0
    ), "Incorrect average turnaround time for case 1."


def test_fcfs_case_1_average_wait_time(case1: FirstComeFirstServeScheduler):
    assert case1.average_wait_time == 5.2, "Incorrect average wait time for case 1."


def test_fcfs_case_2_average_turnaround_time(case2: FirstComeFirstServeScheduler):
    assert (
        case2.average_turnaround_time == 9.4
    ), "Incorrect average turnaround time for case 2."


def test_fcfs_case_2_average_wait_time(case2: FirstComeFirstServeScheduler):
    assert case2.average_wait_time == 6, "Incorrect average wait time for case 2."


def test_fcfs_case_3_average_turnaround_time(case3: FirstComeFirstServeScheduler):
    assert (
        case3.average_turnaround_time == 8.4
    ), "Incorrect average turnaround time for case 3."


def test_fcfs_case_3_average_wait_time(case3: FirstComeFirstServeScheduler):
    assert case3.average_wait_time == 5.2, "Incorrect average wait time for case 3."
