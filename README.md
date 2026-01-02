# The Resistance of Randomness  
### Random Walks and Electric Circuits: A Formal Equivalence

---

## Introduction

This project, **The Resistance of Randomness**, studies a deep and
counterintuitive connection between two seemingly unrelated systems:
**random walks in probability theory** and **electrical circuits in classical
physics**.

A random walk describes the motion of a particle (or agent) that moves
unpredictably across a network. Such processes arise naturally in Markov
chains, graph algorithms, diffusion models, and financial time series.
At first glance, quantities like *hitting time* or *commute time* appear
inherently stochastic and difficult to compute exactly.

Electrical circuits, on the other hand, are governed by deterministic physical
laws such as **Ohm’s Law** and **Kirchhoff’s Current Law**.

The central insight of this project is that these two systems are
**mathematically equivalent**.

By treating a graph as an electrical network—where vertices act as circuit
nodes and edges act as unit resistors—we can compute probabilistic quantities
of random walks using standard tools from circuit theory and linear algebra.
In particular, expected hitting times correspond exactly to nodal voltages
in an equivalent resistive network.

This perspective allows us to replace noisy Monte Carlo estimation with
precise analytical computation using the **graph Laplacian**.

From a quantitative research and HFT perspective, this framework is highly
relevant. Many problems in finance—such as first-passage times, signal decay,
liquidity flow, and risk propagation—can be modeled as random processes on
networks. Understanding when randomness hides deterministic structure is a
core modeling skill.

---

## Core Result: Probability–Physics Duality

The main result explored and verified in this project is the **Commute Time
Identity**:

$$
C_{uv} = 2m \cdot R_{uv}
$$

where:

- \( C_{uv} \) is the expected number of steps for a random walk to travel from
  node \( u \) to node \( v \) and return,
- \( m \) is the total number of edges in the graph,
- \( R_{uv} \) is the effective electrical resistance between nodes \( u \) and
  \( v \) when each edge is treated as a 1Ω resistor.

This identity shows that a fundamentally stochastic quantity can be computed
via a deterministic linear system.

---

## Stochastic Formulation: Random Walks on Graphs

Consider an undirected graph \( G = (V, E) \).

A simple random walk evolves as follows:
- At each step, the walker moves from its current node to a uniformly random
  neighboring node.
- If a node \( x_i \) has degree \( d_i \), each neighbor is chosen with
  probability \( 1 / d_i \).

### Hitting Time

Let \( H_{uv} \) denote the **hitting time**, defined as the expected number of
steps required for a random walk starting at node \( u \) to reach node \( v \).

Let \( E[x_i] \) be the expected number of steps to reach \( v \) starting from
node \( x_i \). For any node \( x_i \neq v \):

$$
E[x_i] = \frac{1}{d_i} \sum_{(x_i, x_j) \in E} E[x_j] + 1
$$

with boundary condition:

$$
E[v] = 0
$$

This system of linear equations fully characterizes the hitting time.

### Commute Time

The **commute time** between nodes \( u \) and \( v \) is defined as:

$$
C_{uv} = H_{uv} + H_{vu}
$$

It represents the expected number of steps for a round trip from \( u \) to
\( v \) and back.

---

## Physical Formulation: Electric Circuits

We now reinterpret the same graph as an electrical network:

- Each edge is replaced by a resistor of resistance 1Ω,
- Each vertex becomes a circuit node with voltage \( V_i \),
- External currents \( I_i \) are injected at nodes.

By Kirchhoff’s Current Law, the nodal equation is:

$$
d_i V_i - \sum_{(x_i, x_j) \in E} V_j = I_i
$$

---

## Establishing the Equivalence

The random walk equations and circuit equations become identical if we make
the identification:

$$
V_i = E[x_i]
$$

and choose external currents:

$$
I_i = d_i \quad \text{for all } i \neq v
$$

Current conservation implies that the total injected current equals:

$$
\sum_i d_i = 2m
$$

where \( m \) is the number of edges in the graph.

Thus, expected hitting times are exactly equal to node voltages in the
corresponding electrical network.

---

## Uniqueness and the Graph Laplacian

The system can be written compactly as:

$$
L V = I
$$

where \( L = D - A \) is the **graph Laplacian**.

Because the Laplacian is singular (voltages are defined only up to an additive
constant), one node is *grounded* by fixing its voltage to zero. This removes
the ambiguity and guarantees a unique solution.

---

## Deriving the Commute Time Identity

To compute the commute time, two circuit configurations are considered:

1. A circuit grounded at node \( v \), yielding \( H_{uv} \)
2. A circuit grounded at node \( u \), yielding \( H_{vu} \)

By reversing currents in the second circuit and applying the superposition
principle, currents cancel at all intermediate nodes. The resulting circuit
has a net current of \( 2m \) flowing from \( u \) to \( v \).

By Ohm’s Law:

$$
V_u - V_v = I \cdot R_{uv}
$$

which directly yields:

$$
C_{uv} = 2m \cdot R_{uv}
$$

---

## Experimental Validation

The theory is validated using Monte Carlo simulation of random walks on a
fixed graph with \( m = 10 \) edges, along with a deterministic computation
of effective resistance using the graph Laplacian.

### Numerical Results

| Quantity | Value |
|--------|-------|
| Hitting Time \( H_{uv} \) | ~13.78 steps |
| Hitting Time \( H_{vu} \) | ~7.68 steps |
| Simulated Commute Time | ~21.46 steps |
| Effective Resistance \( R_{uv} \) | ~1.0652 Ω |
| Theoretical \( 2mR_{uv} \) | ~21.30 steps |

The simulated commute time closely matches the theoretical prediction.

---

## Distribution of Hitting Times

The histogram of hitting times shows:

- A strong concentration at small step counts,
- A pronounced heavy tail caused by rare but long trajectories,
- Asymmetry between \( H_{uv} \) and \( H_{vu} \) driven by graph topology and
  degree imbalance.

This highlights why analytical approaches are often preferable to pure
simulation when studying stochastic systems with high variance.

The histogram image is saved automatically in the `results/` directory.

---

## Relevance to Quantitative Research and HFT

This project connects directly to problems in quantitative finance:

- **First-passage times** for barrier crossings,
- **Liquidity flow** modeled as current through a network,
- **Risk contagion** in correlation and exposure graphs,
- **Spectral properties** of the Laplacian related to mixing and stability.

The ability to translate stochastic dynamics into deterministic linear systems
is a core skill in quantitative research.

---

## How to Run

```bash
pip install networkx numpy matplotlib
python the_resistance_of_randomness.py
