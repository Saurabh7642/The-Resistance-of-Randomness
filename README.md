# The Resistance of Randomness  
### A Formal Equivalence Between Random Walks and Electric Circuits

This repository presents a rigorous analytical and experimental study of the
mathematical equivalence between **discrete-time random walks (Markov chains)**
and **electrical resistor networks**.

By mapping probabilistic states to nodal voltages, the project demonstrates how
stochastic quantities such as **hitting time** and **commute time** can be solved
using deterministic tools from **linear algebra**, specifically the **graph
Laplacian**.

This perspective provides a clean bridge between probability, physics, and
network theory, and is directly relevant to **quantitative research**, where
first-passage times, diffusion, and flow through complex networks frequently
arise.

---

## 🔬 Core Theorem — Probability–Physics Duality

The central result explored and verified in this project is the **Commute Time
Identity**:

\[
\boxed{
C_{uv} = 2m \cdot R_{uv}
}
\]

where:

- \( C_{uv} \) is the expected number of steps for a random walk to travel from
  node \( u \) to node \( v \) and return,
- \( m \) is the total number of edges in the graph,
- \( R_{uv} \) is the effective electrical resistance between \( u \) and \( v \)
  when each edge is treated as a \(1\Omega\) resistor.

This identity reveals that a fundamentally stochastic quantity can be computed
via a deterministic linear system.

---

## 🛠 Analytical Framework

### 1. Stochastic Formulation — Random Walks

A simple random walk is defined on an undirected graph \( G = (V, E) \):

- From node \( x_i \), the walker moves to a uniformly random neighbor with
  probability \( 1/d_i \), where \( d_i \) is the degree of \( x_i \).

**Hitting Time**  
\( H_{uv} \): expected number of steps to reach node \( v \) starting from \( u \).

For any node \( x_i \neq v \), the expected hitting time satisfies:

\[
E[x_i] = \frac{1}{d_i} \sum_{(x_i,x_j) \in E} E[x_j] + 1
\]

with boundary condition:

\[
E[v] = 0
\]

This yields a system of linear equations governing the random walk.

---

### 2. Physical Formulation — Electric Circuits

The same graph is reinterpreted as an electrical network:

- Each edge is replaced by a \(1\Omega\) resistor,
- Each node has a voltage \( V_i \),
- External currents \( I_i \) are injected at nodes.

By Kirchhoff’s Current Law (KCL):

\[
d_i V_i - \sum_{(x_i,x_j) \in E} V_j = I_i
\]

---

### 3. Equivalence via the Laplacian

By identifying:

\[
V_i \equiv E[x_i]
\]

and choosing external currents \( I_i = d_i \) for all \( i \neq v \), the circuit
equations become algebraically identical to the random walk equations.

Current conservation implies that the total injected current equals \(2m\), the
total degree mass of the graph.

---

### 4. Uniqueness and Solvability

The system can be written in matrix form:

\[
L V = I
\]

where \( L = D - A \) is the **graph Laplacian**.

Since the Laplacian is singular (voltages are defined up to a constant), one node
is **grounded** to obtain a unique solution. This guarantees a well-defined
mapping between voltages and expected hitting times.

---

### 5. Commute Time via Superposition

Using linearity and superposition:

- Two circuits (grounded at \( u \) and \( v \)) are combined,
- Currents cancel at all intermediate nodes,
- A net current of \(2m\) flows from \( u \) to \( v \).

By Ohm’s Law \( V = IR \), the voltage difference equals the commute time:

\[
C_{uv} = 2m \cdot R_{uv}
\]

---

## 📊 Experimental Validation

The theory is validated using **Monte Carlo simulation** and **deterministic
Laplacian solves** on a fixed graph with \( m = 10 \) edges.

### Numerical Results

| Quantity | Value |
|------|------|
| \( H_{uv} \) | ~13.78 steps |
| \( H_{vu} \) | ~7.68 steps |
| Simulated \( C_{uv} \) | ~21.46 steps |
| Effective Resistance \( R_{uv} \) | ~1.0652 Ω |
| Theoretical \( 2mR_{uv} \) | ~21.30 steps |

The simulated commute time closely matches the theoretical prediction.

---

### Distributional Behavior (Histogram)

The histogram of hitting times reveals:

- A high-frequency peak at small step counts, indicating many short paths,
- A pronounced **heavy tail**, corresponding to rare but long random trajectories,
- Asymmetry between \( H_{uv} \) and \( H_{vu} \) caused by local degree imbalance
  and graph topology.

This highlights why analytical methods are often preferable to pure Monte Carlo
estimation for first-passage problems.

The histogram is saved automatically to the `results/` directory.

---

## 🚀 Quantitative Research Perspective

This framework is directly relevant to quantitative finance and HFT:

- **First-Passage Times**: Barrier crossings and signal decay
- **Liquidity Flow**: Order books as flow networks with resistance-like friction
- **Risk Contagion**: Shock propagation in correlation and exposure graphs
- **Spectral Methods**: Laplacian eigenvalues relate to mixing time and stability

The project demonstrates the ability to translate stochastic systems into
deterministic representations — a core skill in quantitative research.

---

## ▶️ How to Run

```bash
pip install networkx numpy matplotlib
python the_resistance_of_randomness.py
