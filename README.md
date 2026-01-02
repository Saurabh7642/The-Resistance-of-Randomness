# The Resistance of Randomness  
### Random Walks and Electric Circuits: A Formal Equivalence

---

## 1. Introduction

This project, **The Resistance of Randomness**, explores a deep mathematical
connection between two seemingly unrelated systems: **random walks on graphs**
and **electrical resistor networks**.

Random walks are a fundamental model for uncertainty and diffusion. A walker
moves step by step across a graph, choosing its next position randomly from
the available neighbors. Quantities such as how long it takes to reach a
target, or how long a round trip between two nodes takes on average, appear
inherently stochastic and difficult to analyze exactly.

Electrical circuits, in contrast, are governed by deterministic physical laws
such as Ohm’s Law and Kirchhoff’s Current Law.

The central idea of this project is that these two systems are, in fact,
**mathematically equivalent**. By treating a graph as an electrical network,
we can compute probabilistic quantities of random walks using linear algebra
and classical circuit theory.

---

## 2. Overview of the Core Idea

The key observation is the following correspondence:

- Graph vertices correspond to circuit nodes  
- Graph edges correspond to resistors of unit resistance  
- Expected hitting times correspond to node voltages  

Under this interpretation, quantities from probability theory can be computed
by solving a deterministic system of linear equations involving the
**graph Laplacian**.

This transformation allows random walk behavior to be analyzed without relying
solely on simulation.

---

## 3. Random Walk Formulation

Consider an undirected graph \( G = (V, E) \).

A simple random walk evolves as follows:
- At each step, the walker moves from its current node to one of its neighbors.
- Each neighbor is chosen uniformly at random.

If a node \( x_i \) has degree \( d_i \), then each neighbor is chosen with
probability \( 1 / d_i \).

---

### 3.1 Hitting Time

The **hitting time** from node \( u \) to node \( v \) is defined as the expected
number of steps required for a random walk starting at \( u \) to reach \( v \)
for the first time.

Let \( E(x_i) \) denote the expected number of steps required to reach the
target node \( v \) starting from node \( x_i \).

For any node \( x_i \neq v \), the expectation satisfies the recurrence:

$$
E(x_i) = \frac{1}{d_i} \sum_{(x_i, x_j) \in E} E(x_j) + 1
$$

The boundary condition is:

$$
E(v) = 0
$$

This system of equations fully determines the hitting times.

---

### 3.2 Commute Time

The **commute time** between nodes \( u \) and \( v \) is defined as the expected
number of steps for a round trip:

$$
C(u, v) = H(u, v) + H(v, u)
$$

where:
- \( H(u, v) \) is the hitting time from \( u \) to \( v \),
- \( H(v, u) \) is the hitting time from \( v \) to \( u \).

---

## 4. Electrical Circuit Interpretation

We now reinterpret the same graph as an electrical circuit:

- Each edge is replaced by a resistor of resistance 1 ohm  
- Each vertex becomes a node in the circuit  
- Each node is assigned a voltage \( V_i \)  

According to Kirchhoff’s Current Law, the total current leaving a node must
equal the externally injected current at that node.

This leads to the nodal equation:

$$
d_i V_i - \sum_{(x_i, x_j) \in E} V_j = I_i
$$

where \( I_i \) denotes the external current injected at node \( i \).

---

## 5. Establishing the Equivalence

The random walk equations and the circuit equations become identical if we make
the identification:

$$
V_i = E(x_i)
$$

and choose the injected currents as:

$$
I_i = d_i \quad \text{for all nodes except the target}
$$

With this choice, the equations governing voltages exactly match the equations
governing expected hitting times.

Because the sum of all node degrees in a graph equals twice the number of
edges, the total injected current satisfies:

$$
\sum_i d_i = 2m
$$

where \( m \) is the number of edges in the graph.

---

## 6. The Graph Laplacian and Uniqueness

The system of equations can be written compactly as:

$$
L V = I
$$

where \( L = D - A \) is the **graph Laplacian**, with \( D \) the degree matrix
and \( A \) the adjacency matrix.

The Laplacian matrix is singular, reflecting the fact that voltages are defined
only up to an additive constant. To obtain a unique solution, one node is
**grounded** by fixing its voltage to zero.

This removes the ambiguity and ensures a well-defined solution.

---

## 7. Derivation of the Commute Time Identity

To derive the commute time, two circuit configurations are considered:

1. A circuit grounded at node \( v \), yielding the hitting time from \( u \) to \( v \)
2. A circuit grounded at node \( u \), yielding the hitting time from \( v \) to \( u \)

By reversing the currents in the second circuit and applying the superposition
principle, currents cancel at all intermediate nodes. The resulting circuit has
a net current of \( 2m \) flowing from \( u \) to \( v \).

By Ohm’s Law, the voltage difference satisfies:

$$
V_u - V_v = I \cdot R(u, v)
$$

This leads to the **commute time identity**:

$$
C(u, v) = 2m \cdot R(u, v)
$$

where \( R(u, v) \) is the effective electrical resistance between nodes
\( u \) and \( v \).

---

## 8. Experimental Validation

The theoretical results are validated using Monte Carlo simulation of random
walks on a fixed graph with \( m = 10 \) edges, along with a deterministic
computation of effective resistance using the Laplacian matrix.

### Numerical Results

| Quantity | Value |
|--------|-------|
| Hitting time from U to V | ~13.78 steps |
| Hitting time from V to U | ~7.68 steps |
| Simulated commute time | ~21.46 steps |
| Effective resistance | ~1.0652 ohms |
| Theoretical commute time | ~21.30 steps |

The simulated and theoretical commute times are in close agreement.

---

## 9. Distribution of Hitting Times

The histogram of hitting times reveals several important features:

- A strong concentration at small step counts, indicating many short paths  
- A pronounced heavy tail caused by rare but long trajectories  
- Asymmetry between the two directions due to local graph structure  

This behavior illustrates why average values alone are often insufficient to
fully characterize random processes.

The histogram generated by the simulation is saved in the `results/` directory.

---

## 10. How to Run

```bash
pip install networkx numpy matplotlib
python the_resistance_of_randomness.py
