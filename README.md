# The Resistance of Randomness  
### Random Walks and Electric Circuits: A Formal Equivalence

---

## 1. Introduction and Motivation

Randomness plays a central role in many systems studied in computer science,
physics, and quantitative finance. Random walks on graphs, in particular,
serve as a foundational model for diffusion, exploration, and uncertainty.
They appear naturally in areas such as Markov chains, network routing,
PageRank-style algorithms, and price dynamics in financial markets.

A natural question arises when studying random walks:

**How long does it take, on average, for a random process to reach a target and return?**

This question leads to the concept of *hitting time* and *commute time*.
At first glance, these quantities appear inherently probabilistic and
difficult to compute exactly.

The central goal of this project is to show that these seemingly random
quantities admit a precise analytical structure when viewed from a different
perspective — **electrical network theory**.

---

## 2. Overview of the Core Idea

The key insight explored in this project is that **random walks on graphs are
mathematically equivalent to electrical circuits**.

By interpreting:
- graph vertices as circuit nodes,
- graph edges as resistors,
- expected hitting times as voltages,

we can transform a stochastic problem into a deterministic one governed by
linear algebra.

This equivalence allows us to compute random walk quantities using the
**graph Laplacian**, a fundamental object in spectral graph theory.

---

## 3. Stochastic Formulation: Random Walks on Graphs

Consider an undirected graph \( G = (V, E) \).

A *simple random walk* on this graph evolves as follows:
- At each step, the walker moves from its current node to one of its neighbors.
- Each neighbor is chosen uniformly at random.

If a node \( x_i \) has degree \( d_i \), then each neighboring node is chosen
with probability \( 1 / d_i \).

---

### 3.1 Hitting Time

The **hitting time** \( H_{uv} \) is defined as the expected number of steps
required for a random walk starting at node \( u \) to reach node \( v \)
for the first time.

Let \( E[x_i] \) denote the expected number of steps required to reach the
target node \( v \) starting from node \( x_i \).

For any node \( x_i \neq v \), the expectation satisfies:

$$
E[x_i] = \frac{1}{d_i} \sum_{(x_i, x_j) \in E} E[x_j] + 1
$$

The boundary condition is:

$$
E[v] = 0
$$

This system of equations fully characterizes the hitting time.

---

### 3.2 Commute Time

The **commute time** between nodes \( u \) and \( v \) is defined as:

$$
C_{uv} = H_{uv} + H_{vu}
$$

It represents the expected number of steps for a random walk to travel from
\( u \) to \( v \) and then return to \( u \).

---

## 4. Physical Interpretation: Electric Circuits

We now reinterpret the same graph as an electrical network:

- Each edge is replaced by a resistor of resistance 1Ω.
- Each vertex becomes a node in the circuit.
- Each node is assigned a voltage \( V_i \).

According to Kirchhoff’s Current Law, the total current flowing out of a node
must equal the externally injected current.

This yields the nodal equation:

$$
d_i V_i - \sum_{(x_i, x_j) \in E} V_j = I_i
$$

---

## 5. Establishing the Equivalence

The random walk equations and circuit equations become identical if we make
the following identification:

$$
V_i = E[x_i]
$$

and choose external currents:

$$
I_i = d_i \quad \text{for all } i \neq v
$$

With this choice, the equations governing voltages exactly match the equations
governing expected hitting times.

Current conservation implies that the total injected current equals:

$$
\sum_i d_i = 2m
$$

where \( m \) is the number of edges in the graph.

---

## 6. Uniqueness and the Graph Laplacian

The system can be written compactly as:

$$
L V = I
$$

where \( L = D - A \) is the **graph Laplacian**.

The Laplacian matrix is singular because voltages are only defined up to an
additive constant. To obtain a unique solution, one node is *grounded* by
fixing its voltage to zero.

This guarantees a unique solution for the voltages, and hence for the expected
hitting times.

---

## 7. Deriving the Commute Time Identity

To compute the commute time, two circuit configurations are considered:

1. A circuit grounded at node \( v \), yielding \( H_{uv} \)
2. A circuit grounded at node \( u \), yielding \( H_{vu} \)

By reversing currents in the second circuit and applying the superposition
principle, currents cancel at all intermediate nodes.

The resulting circuit has a net current of \( 2m \) flowing from \( u \) to \( v \).

By Ohm’s Law:

$$
V_u - V_v = I \cdot R_{uv}
$$

This yields the central identity:

$$
C_{uv} = 2m \cdot R_{uv}
$$

---

## 8. Experimental Validation

To validate the theory, we perform a Monte Carlo simulation of random walks
on a fixed graph with \( m = 10 \) edges.

### 8.1 Simulation Results

| Quantity | Value |
|--------|-------|
| Hitting Time \( H_{uv} \) | ~13.78 steps |
| Hitting Time \( H_{vu} \) | ~7.68 steps |
| Simulated Commute Time | ~21.46 steps |
| Effective Resistance \( R_{uv} \) | ~1.0652 Ω |
| Theoretical \( 2mR_{uv} \) | ~21.30 steps |

The simulated commute time closely matches the theoretical prediction.

---

### 8.2 Distribution of Hitting Times

The histogram of hitting times reveals:

- A strong concentration at low step counts
- A pronounced heavy tail caused by rare but long random trajectories
- Asymmetry between \( H_{uv} \) and \( H_{vu} \) driven by graph topology

This highlights why analytical approaches are essential for understanding
stochastic systems with high variance.

---

## 9. Relevance to Quantitative Research

This project directly connects to problems encountered in quantitative finance:

- **First-passage times** for barrier crossings
- **Liquidity flow** in networked order books
- **Risk contagion** in correlation and exposure graphs
- **Spectral properties** of the Laplacian related to stability and mixing

The ability to translate stochastic dynamics into deterministic linear systems
is a core skill in quantitative research and high-frequency trading.

---

## 10. How to Run

```bash
pip install networkx numpy matplotlib
python the_resistance_of_randomness.py
