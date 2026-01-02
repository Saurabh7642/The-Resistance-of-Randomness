# The Resistance of Randomness  
### Isomorphism of Random Walks and Electrical Potential Theory

---

## Abstract

This project studies a classical but profound equivalence between random walks
on graphs and electrical resistor networks. By mapping expected hitting times
of a random walk to nodal voltages in an equivalent electrical circuit, the
work shows that commute times in Markov chains can be computed deterministically
using the graph Laplacian. Theoretical results are derived step by step and
validated through Monte Carlo simulation, illustrating how stochastic
processes often admit precise analytical structure.

---

## 1. Introduction

Randomness plays a central role in many systems studied in mathematics,
computer science, and physics. Random walks on graphs, in particular, serve
as a fundamental model for diffusion, exploration, and uncertainty. They
appear naturally in Markov chains, network processes, and a wide range of
algorithmic and physical systems.

A basic but nontrivial question when studying random walks is:

*How long does it take, on average, for a random process to reach a target
and return?*

At first glance, quantities such as hitting time and commute time appear
inherently probabilistic and difficult to compute exactly. One might expect
simulation to be the only practical tool.

Electrical circuits, by contrast, are governed by deterministic physical laws
such as Ohm’s Law and Kirchhoff’s Current Law.

The central idea of this project is that these two systems are not merely
analogous, but **mathematically equivalent**. By interpreting a graph as an
electrical network, probabilistic questions about random walks can be answered
using linear algebra and classical circuit theory.

---

## 2. Problem Statement

Given an undirected graph and two vertices \( u \) and \( v \), determine the
expected number of steps required for a random walk to travel from \( u \) to
\( v \) and then return to \( u \).

The objective is to:
1. Formally derive this quantity,
2. Express it in closed form using deterministic methods,
3. Validate the result through simulation.

---

## 3. Assumptions and Scope

The analysis in this project is conducted under the following assumptions:

- The graph is undirected and connected,
- All edges have unit weight,
- The random walk is discrete-time and simple (uniform transition
  probabilities).

Extensions to weighted graphs or continuous-time random walks are not
considered here, but the framework generalizes naturally.

---

## 4. Random Walk Formulation

Consider an undirected graph \( G = (V, E) \).

A simple random walk evolves as follows:
- At each step, the walker moves from its current node to one of its neighbors,
  chosen uniformly at random.
- If a node \( x_i \) has degree \( d_i \), each neighbor is chosen with
  probability \( 1 / d_i \).

---

### 4.1 Hitting Time

The **hitting time** from node \( u \) to node \( v \) is defined as the expected
number of steps required for a random walk starting at \( u \) to reach \( v \)
for the first time.

Let \( E(x_i) \) denote the expected number of steps to reach \( v \) starting
from node \( x_i \). For any node \( x_i \neq v \):

$$
E(x_i) = \frac{1}{d_i} \sum_{(x_i, x_j) \in E} E(x_j) + 1
$$

The boundary condition is:

$$
E(v) = 0
$$

This recurrence uniquely characterizes the hitting times.

---

### 4.2 Commute Time

The **commute time** between nodes \( u \) and \( v \) is defined as:

$$
C(u, v) = H(u, v) + H(v, u)
$$

It represents the expected number of steps for a random walk to travel from
\( u \) to \( v \) and then return.

---

## 5. Electrical Circuit Interpretation

The same graph can be reinterpreted as an electrical circuit:

- Each edge is replaced by a resistor of resistance 1 ohm,
- Each vertex becomes a node in the circuit,
- Each node is assigned a voltage \( V_i \).

By Kirchhoff’s Current Law, the total current leaving a node must equal the
externally injected current at that node. This yields the nodal equation:

$$
d_i V_i - \sum_{(x_i, x_j) \in E} V_j = I_i
$$

where \( I_i \) denotes the external current injected at node \( i \).

---

## 6. Establishing the Equivalence

The random walk equations and circuit equations become identical if we make
the identification:

$$
V_i = E(x_i)
$$

and choose the injected currents as:

$$
I_i = d_i \quad \text{for all nodes except the target}
$$

Since the sum of all node degrees in a graph equals twice the number of edges,
the total injected current satisfies:

$$
\sum_i d_i = 2m
$$

where \( m \) is the number of edges in the graph.

Thus, expected hitting times correspond exactly to node voltages in the
equivalent electrical network.

---

## 7. The Graph Laplacian and Uniqueness

The system can be written compactly as:

$$
L V = I
$$

where \( L = D - A \) is the **graph Laplacian**, with \( D \) the degree matrix
and \( A \) the adjacency matrix.

The Laplacian is singular because voltages are defined only up to an additive
constant. To obtain a unique solution, one node is **grounded** by fixing its
voltage to zero.

---

## 8. Deriving the Commute Time Identity

To compute the commute time, two circuit configurations are considered:

1. A circuit grounded at node \( v \), yielding the hitting time from \( u \) to \( v \),
2. A circuit grounded at node \( u \), yielding the hitting time from \( v \) to \( u \).

By reversing currents in the second circuit and applying the superposition
principle, currents cancel at all intermediate nodes. The resulting circuit
has a net current of \( 2m \) flowing from \( u \) to \( v \).

By Ohm’s Law:

$$
V_u - V_v = I \cdot R(u, v)
$$

This yields the **commute time identity**:

$$
C(u, v) = 2m \cdot R(u, v)
$$

where \( R(u, v) \) is the effective electrical resistance between nodes
\( u \) and \( v \).

---

## 9. Methodology

The project proceeds along two parallel approaches:

1. **Simulation**: Random walks are simulated directly to estimate hitting
   times using Monte Carlo sampling.
2. **Analytical computation**: Effective resistance is computed by solving a
   reduced Laplacian linear system with one node grounded.

These two approaches are implemented independently and compared numerically.

---

## 10. Experimental Validation

The theory is validated on a fixed graph with \( m = 10 \) edges.

### Numerical Results

| Quantity | Value |
|--------|-------|
| Hitting time from U to V | ~13.78 steps |
| Hitting time from V to U | ~7.68 steps |
| Simulated commute time | ~21.46 steps |
| Effective resistance | ~1.0652 ohms |
| Theoretical commute time | ~21.30 steps |

The simulated and theoretical values are in close agreement.

---

## 11. Distribution of Hitting Times

The histogram of hitting times reveals:

- A strong concentration at small step counts,
- A pronounced heavy tail caused by rare but long trajectories,
- Directional asymmetry driven by local graph structure.

This behavior highlights the limitations of relying solely on average values
when analyzing stochastic processes.

<img width="859" height="547" alt="image" src="https://github.com/user-attachments/assets/cbb9dfe1-4f5c-4e5e-ba3d-2a2f99da65e5" />

---

## 12. Computational Considerations

Monte Carlo simulation converges slowly due to the heavy-tailed nature of
hitting time distributions. In contrast, the Laplacian-based approach computes
commute time via a single linear system solve.

For larger graphs, sparse linear solvers would be required to ensure
scalability.

---

## 13. Historical Context

The equivalence between random walks and electrical networks has classical
roots, notably in the work of Doyle and Snell. This project focuses on
understanding, deriving, and validating this result rather than presenting it
as a novel discovery.

---

## 14. How to Run

```bash
pip install networkx numpy matplotlib
python the_resistance_of_randomness.py
