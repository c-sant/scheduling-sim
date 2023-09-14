# Simulador de Escalonador  de Processos

![Test Status](https://github.com/c-sant/scheduling-sim/actions/workflows/pytest.yml/badge.svg)

Um projeto desenvolvido em Python para simular algoritmos de escalonamento usados por
sistemas operacionais.

## Tabela de Conteúdos

- [Algoritmos Implementados](#algoritmos-implementados)
- [Instalação](#instalação)

## Algoritmos Implementados

Até o momento, o simulador suporta os seguintes algoritmos:

- [X] **FCFS**: First Come First Serve
- [X] **SJF**: Shortest Job First
- [ ] **SRTF**: Shortest Remaining Time First
- [ ] **RR**: Round Robin
- [ ] **PRIOc**: Priority (Cooperative)
- [ ] **PRIOp**: Priority (Preemptive) 

## Instalação

1. Clone o repositório em sua máquina local.

```shell
git clone https://github.com/c-sant/scheduling-sim.git
```

2. Acesse o diretório do projeto.

```shell
cd scheduling-sim
```

3. Crie um ambiente virtual (opcional, mas recomendado):

```shell
python -m venv venv
```

4. Ative seu ambiente virtual:

* No Windows:

```shell
venv\Scripts\activate
```

* No macOS e no Linux:

```shell
source venv/bin/activate
```

5. Instale as dependências do projeto:

```shell
pip install -r requirements.txt
```