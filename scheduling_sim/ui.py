import os
import re

import pandas as pd
import PySimpleGUI as sg

from scheduling_sim import (
    FirstComeFirstServeScheduler,
    PriorityCooperativeScheduler,
    PriorityPreemptiveScheduler,
    Process,
    RoundRobinScheduler,
    SchedulingAlgorithm,
    ShortestJobFirstScheduler,
    ShortestRemainingTimeFirstScheduler,
)


class SchedulingSimulatorAPP:
    algorithms: dict[str, type] = {
        "First Come First Serve": FirstComeFirstServeScheduler,
        "Shortest Job First": ShortestJobFirstScheduler,
        "Priority (Cooperative)": PriorityCooperativeScheduler,
        "Round Robin": RoundRobinScheduler,
        "Shortest Remaining Time First": ShortestRemainingTimeFirstScheduler,
        "Priority (Preemptive)": PriorityPreemptiveScheduler,
    }

    def __init__(self):
        self._set_default_values()
        self._build_layout()

    def run(self):
        window = sg.Window("Scheduling Simulator", self.layout, resizable=True)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, "Exit"):
                break

            if event == "-ALGORITHM-":
                self._current_scheduler_type = values["-ALGORITHM-"]

                window["-PRIORITY-"].update(
                    disabled=(not values["-ALGORITHM-"].startswith("Priority"))
                )

                window["-QUANTUM-"].update(
                    disabled=values["-ALGORITHM-"] != "Round Robin"
                )

            if event == "-INPUT-":
                self._input_path = values["-INPUT-"]

            if event == "-OUTPUT-":
                self._input_path = values["-OUTPUT-"]

            if event == "-QUANTUM-":
                quantum_has_non_numeric_value = bool(
                    re.search(r"[^0-9]", values["-QUANTUM-"])
                )

                if len(values["-QUANTUM-"]) == 0:
                    window["-QUANTUM-"].update("0")
                elif quantum_has_non_numeric_value:
                    is_digit = lambda x: x in "0123456789"
                    quantum_value = "".join(filter(is_digit, values["-QUANTUM-"]))
                    window["-QUANTUM-"].update(quantum_value)

            if event == "-EXECUTE-":
                self._update_metrics(window, values)
                self._export_execution_report()

        window.close()

    def _set_default_values(self):
        self._output_path = "data\\output"
        self._input_path = "data\\input\\processes.xlsx"
        self._current_scheduler_type = "First Come First Serve"

    def _build_layout(self):
        self.layout = [
            # Input section
            [
                sg.Text("Input file:"),
                sg.InputText(
                    key="-INPUT-",
                    enable_events=True,
                    expand_x=True,
                    default_text=self._input_path,
                ),
                sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),)),
            ],
            [
                sg.Text("Output folder:"),
                sg.InputText(
                    key="-OUTPUT-",
                    enable_events=True,
                    expand_x=True,
                    default_text=self._output_path,
                ),
                sg.FolderBrowse(),
            ],
            [sg.HSeparator()],
            [
                # Configurations section
                sg.Column(
                    [
                        [
                            sg.Text("Algorithm:"),
                            sg.Combo(
                                list(self.algorithms.keys()),
                                key="-ALGORITHM-",
                                enable_events=True,
                                default_value=list(self.algorithms.keys())[0],
                            ),
                        ],
                        [
                            sg.Text("Priority order:"),
                            sg.Combo(
                                ["Ascending", "Descending"],
                                key="-PRIORITY-",
                                enable_events=True,
                                disabled=True,
                                default_value="Descending",
                            ),
                        ],
                        [
                            sg.Text("Quantum length:"),
                            sg.InputText(
                                key="-QUANTUM-",
                                enable_events=True,
                                default_text="0",
                                size=(10, 1),
                                disabled=True,
                            ),
                        ],
                        [sg.Button("Execute", key="-EXECUTE-")],
                    ]
                ),
                sg.VSeparator(),
                # Metrics section
                sg.Column(
                    [
                        [
                            sg.Text("Average wait time:"),
                            sg.Text("", key="-AVG_WAIT-"),
                        ],
                        [
                            sg.Text("Average turnaround time:"),
                            sg.Text("", key="-AVG_TURNAROUND-"),
                        ],
                        [
                            sg.Text("Best wait time:"),
                            sg.Text("", key="-BEST_WAIT-"),
                        ],
                    ]
                ),
            ],
        ]

    def _update_metrics(self, window: sg.Window, values: dict[str,]):
        scheduler = self._create_scheduler()

        window["-AVG_WAIT-"].update(scheduler.average_wait_time)
        window["-AVG_TURNAROUND-"].update(scheduler.average_turnaround_time)
        window["-BEST_WAIT-"].update(self._determine_best_wait_time())

    def _create_scheduler(self) -> SchedulingAlgorithm:
        processes = self._read_processes_table()
        scheduler_type = self.algorithms[self._current_scheduler_type]
        scheduler = scheduler_type(processes)

        return scheduler

    def _read_processes_table(self) -> list[Process]:
        processes_df = pd.read_excel(self._input_path)
        processes = []

        for process in processes_df.to_dict(orient="records"):
            processes.append(
                Process(
                    name=process["Process Name"],
                    arrival_time=process["Arrival Time"],
                    execution_time=process["Execution Time"],
                    priority_level=process["Priority Level"],
                )
            )

        return processes

    def _determine_best_wait_time(self) -> str:
        algorithm_times = []
        processes = self._read_processes_table()

        for algorithm_name, scheduler_type in self.algorithms.items():
            scheduler = scheduler_type(processes)

            algorithm_times.append(
                {
                    "algorithm_name": algorithm_name,
                    "wait_time": scheduler.average_wait_time,
                }
            )

        best_wait_time_algorithm = sorted(
            algorithm_times, key=lambda algorithm: algorithm["wait_time"]
        )[0]

        return f"{best_wait_time_algorithm['algorithm_name']} ({best_wait_time_algorithm['wait_time']})"

    def _export_execution_report(self):
        file_path = os.path.join(self._output_path, "execution_report.xlsx")
        scheduler = self._create_scheduler()

        execution_report = scheduler.run()
        execution_report.to_excel(file_path, index=False)
