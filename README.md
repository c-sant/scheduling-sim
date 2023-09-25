# Process Scheduler Simulator

![Test Status](https://github.com/c-sant/scheduling-sim/actions/workflows/pytest.yml/badge.svg)
Python version: **3.11**

A Python project developed to simulate scheduling algorithms used by Operational
Systems.

## Table of Contents

  - [To-Do List](#to-do-list)
  - [Implemented Algorithms](#implemented-algorithms)
  - [Instalation](#instalation)

## To-Do List

- [X] Implement provisioned algorithms.
- [X] Add documentation for the implemented algorithms.
- [X] Create tests for the implemented algorithms
- [X] Add documentation for the test classes.
- [X] Make a Graphical User Interface.
- [ ] Add documentation for the Graphical User Interface.

## Implemented Algorithms

So far, the simulator supports the following algorithms:

- [X] **FCFS**: First Come First Serve
- [X] **SJF**: Shortest Job First
- [X] **SRTF**: Shortest Remaining Time First
- [X] **RR**: Round Robin
- [X] **PRIOc**: Priority (Cooperative)
- [X] **PRIOp**: Priority (Preemptive) 

## Instalation

1. Clone the repository to your local machine.

```shell
git clone https://github.com/c-sant/scheduling-sim.git
```

2. Access the project directory.

```shell
cd scheduling-sim
```

3. Create a virtual environment (optional, yet recommended):

```shell
python -m venv venv
```

4. Activate your virtual environment:

* For Windows:

```shell
venv\Scripts\activate
```

* For macOS and Linux:

```shell
source venv/bin/activate
```

5. Install project dependencies:

```shell
pip install -r requirements.txt
```

After all these steps, the project should be good to go. Just execute the `main.py`
file and the user interface will be shown.