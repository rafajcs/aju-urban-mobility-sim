# Aracaju Mobility Simulation

> **Multimodal Simulation and Heuristic Evaluation of Urban Mobility Scenarios: The South Zone – UFS São Cristóvão Corridor**

Research project investigating hypothetical urban mobility policies in Aracaju and São Cristóvão, Sergipe, Brazil, through **microscopic traffic simulation** and **Artificial Intelligence techniques**.

The initial study focuses on the corridor connecting the **South Zone of Aracaju** to the **Federal University of Sergipe (UFS) campus in São Cristóvão**.

---

## Overview

Urban mobility policies can produce complex effects across different transportation modes. This project aims to use traffic simulation as a controlled environment for investigating such effects without requiring interventions in the real transportation system.

The project combines:

* **Eclipse SUMO** for microscopic traffic simulation;
* **Python + TraCI** for simulation control and data collection;
* **Heuristic search** for route planning;
* **Agent-based decision models** for multimodal behavior;
* **Heuristic optimization** for traffic signal control and other interventions.

The initial objective is not to model the entire city, but to develop and validate a **reproducible case study** around the South Zone–UFS corridor.

---

## Research Question

The central question is:

> **How do hypothetical mobility policies affect the performance of a real urban transportation corridor under multimodal traffic simulation?**

Possible extensions include investigating:

* route selection;
* modal choice;
* congestion;
* public transportation performance;
* cycling infrastructure;
* traffic signal optimization.

---

## Methodology

The project follows an incremental methodology.

```text
OpenStreetMap
      │
      ▼
SUMO Network
      │
      ▼
Traffic Demand
      │
      ▼
SUMO Simulation
      │
     TraCI
      │
      ▼
Python
      │
 ┌────┴─────┐
 ▼          ▼
AI       Analysis
 │          │
 └────┬─────┘
      ▼
Experimental Results
```

The first stage focuses exclusively on constructing and validating the simulation environment.

Advanced AI techniques will only be introduced after the baseline model is sufficiently reliable.

---

## Experimental Scenarios

The initial scenarios are:

### C0 — Baseline

Representation of the reference transportation system, using estimated or synthetic demand where appropriate.

### C1 — Public Transportation Priority

Hypothetical interventions such as:

* dedicated bus lanes;
* increased bus frequency;
* traffic signal priority.

### C2 — Cycling-Oriented Mobility

Hypothetical expansion of segregated cycling infrastructure and changes in modal demand.

### C3 — Private Vehicle Restriction

Controlled reductions in private vehicle demand to investigate their effects on the transportation network.

### C4 — Adaptive Traffic Signals

Dynamic traffic signal control based on network conditions such as queues, waiting times, and public transportation demand.

The scenarios are hypotheses for experimentation and do not represent proposed real-world policies.

---

## AI Techniques

The project will progressively investigate classical AI methods.

### Heuristic Search

* Dijkstra;
* Uniform-Cost Search;
* A*;
* multimodal cost functions.

A basic A* formulation is:

$$
f(n)=g(n)+h(n)
$$

where \(g(n)\) represents the accumulated cost and \(h(n)\) the estimated remaining cost.

### Agent-Based Decision Making

Simulated users may select transportation modes and routes according to utility functions involving factors such as:

* travel time;
* distance;
* transfers;
* generalized cost.

### Optimization

Potential methods include:

* Hill Climbing;
* Genetic Algorithms;
* multi-objective optimization.

These methods may eventually be applied to traffic signal control and other configurable parameters.

---

## Evaluation

Scenarios will be compared using quantitative metrics such as:

* travel time;
* waiting time;
* average speed;
* queue length;
* time loss;
* network throughput;
* bus travel time and delay;
* cycling travel time;
* completed trips.

Experiments will use multiple random seeds when stochastic behavior is present.

Results will be reported using appropriate statistical summaries rather than relying on a single simulation run.

---

## Technology Stack

| Component            | Technology     |
| -------------------- | -------------- |
| Traffic simulation   | Eclipse SUMO   |
| Programming          | Python         |
| Simulation interface | TraCI          |
| Geographic data      | OpenStreetMap  |
| Data analysis        | Pandas / NumPy |
| Visualization        | Matplotlib     |
| Version control      | Git            |

Additional libraries will be introduced as required by the experiments.

---

## Repository Structure

```text
aracaju-mobility/
├── data/          # Input data and demand
├── sumo/          # SUMO networks and scenarios
├── src/           # Simulation and analysis code
├── experiments/   # Experiment configurations
├── results/       # Generated results
├── docs/          # Scientific and technical documentation
├── tests/         # Tests
├── README.md
└── requirements.txt
```

---

## Development Roadmap

### Stage 1 — Simulation Infrastructure

* [ ] Set up SUMO environment
* [ ] Create a minimal simulation
* [ ] Integrate Python with TraCI
* [ ] Collect simulation metrics
* [ ] Automate experiments
* [ ] Import the Aracaju/São Cristóvão network
* [ ] Build and validate the baseline scenario

### Stage 2 — Classical AI

* [ ] Implement Dijkstra
* [ ] Implement A*
* [ ] Define multimodal cost functions
* [ ] Compare routing strategies

### Stage 3 — Multimodal Agents

* [ ] Model heterogeneous users
* [ ] Implement modal choice
* [ ] Evaluate emergent network behavior

### Stage 4 — Optimization

* [ ] Traffic signal optimization
* [ ] Hill Climbing experiments
* [ ] Genetic Algorithm experiments
* [ ] Multi-objective evaluation

### Stage 5 — Extended Analysis

* [ ] Advanced scenario comparison
* [ ] Sensitivity analysis
* [ ] Statistical evaluation
* [ ] Optional LLM/VLM-assisted qualitative analysis

---

## Reproducibility

Reproducibility is a core requirement of the project.

Experiments should record:

* scenario;
* random seed;
* simulation parameters;
* demand parameters;
* software versions;
* AI parameters;
* generated metrics.

The project will distinguish clearly between **real-world data**, **estimated parameters**, and **hypothetical assumptions**.

---

## Current Status

**Status:** Early development

The current priority is **Stage 1 — Simulation Infrastructure**.

The project is being developed incrementally, with emphasis on methodological rigor, reproducibility, and compatibility with future scientific publication.

---

## Scientific Goal

The long-term goal is to develop a reproducible framework for evaluating hypothetical urban mobility scenarios through simulation and Artificial Intelligence.

The results may eventually be consolidated into a scientific paper following the **Brazilian Computer Society (SBC)** publication format.

Detailed methodology, experimental decisions, assumptions, and results will be maintained separately in [`docs/`](docs/).

---

## License

To be defined.
