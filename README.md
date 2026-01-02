# The Resistance of Randomness  
### A Formal Equivalence Between Random Walks and Electric Circuits

This repository presents a rigorous analytical and experimental study of the
equivalence between **discrete-time random walks (Markov chains)** and
**electrical resistor networks**.

By mapping probabilistic states to nodal voltages, the project shows how
stochastic quantities such as **hitting time** and **commute time** can be
computed using deterministic linear-algebraic tools, specifically the
**graph Laplacian**.

This perspective is directly relevant to **quantitative research**, where
first-passage times, diffusion, and flow through complex networks frequently
arise.

---

## 🔬 Core Theorem — Probability–Physics Duality

The central result explored in this project is the **Commute Time Identity**:

$$
C_{uv} = 2m \cdot R_{uv}
$$

where:

- **C_uv** is the expected number of steps for a random walk to travel from
  node *u* to node *v* and return,
- **m** is the total number of edges in the graph,
- **R_uv** is the effective electrical resistance between *u* and *v* when
  each edge is treated as a 1Ω resistor.

This identity shows that a stochastic quantity can be computed through a
deterministic linear system.

---

## 🛠 Analytical Framework

### 1. Stochastic Formulation — Random Walks

A simple random walk is defined on an undirected graph **G = (V, E)**.

From node *x_i*, the walker moves to a uniformly random neighbor with probability
**1 / d_i**, where *d_i* is the degree of *x_i*.

**Hitting Time**

H_uv is defined as the expected number of steps to reach node *v* starting from
node *u*.

For any node *x_i ≠ v*, the expected hitting time satisfies:

$$
E[x_i] = \frac{1}{d_i} \sum_{(x_i, x_j) \in E} E[x_j] + 1
$$

with boundary condition:

$$
E[v] = 0
$$

This yields a system of linear equations governing the random walk.

---

### 2. Physical Formulation — Electric Circuits

The same graph is reinterpreted as an electrical network:

- Each edge is replaced with a 1Ω resistor,
- Each node has a voltage *V_i*,
- External currents *I_i* are injected at nodes.

By Kirchhoff’s Current Law:

$$
d_i V_i - \sum_{(x_i, x_j) \in E} V_j = I_i
$$

---

### 3. Equivalence via the Graph Laplacian

By identifying:

$$
V_i = E[x_i]
$$

and choosing external currents **I_i = d_i** for all nodes except the target,
the circuit equations become identical to the random walk equations.

Current conservation implies that the total injected current equals **2m**, the
total degree mass of the graph.

---

### 4. Uniqueness and Solvability

The system can be written in matrix form:

$$
L V = I
$$

where **L = D − A** is the graph Laplacian.

Since the Laplacian is singular (voltages are defined up to a constant), one node
is **grounded** to obtain a unique solution.

---

### 5. Commute Time via Superposition

Using linearity and superposition:

- Two circuits (grounded at *u* and *v*) are combined,
- Currents cancel at all intermediate nodes,
- A net current of **2m** flows from *u* to *v*.

By Ohm’s Law:

$$
V_u - V_v = I \cdot R_{uv}
$$

which gives:

$$
C_{uv} = 2m \cdot R_{uv}
$$

---

## 📊 Experimental Validation

The theory is validated using **Monte Carlo simulation** and deterministic
Laplacian solves on a graph with **m = 10** edges.

### Numerical Results

| Quantity | Value |
|--------|-------|
| H_uv | ~13.78 steps |
| H_vu | ~7.68 steps |
| Simulated C_uv | ~21.46 steps |
| Effective Resistance R_uv | ~1.0652 Ω |
| Theoretical 2mR_uv | ~21.30 steps |

---

### Distributional Behavior

The histogram of hitting times shows:

- A strong peak at small step counts (many short paths),
- A clear **heavy tail**, corresponding to rare but long trajectories,
- Asymmetry between H_uv and H_vu caused by graph topology and degree imbalance.

The histogram image is saved in the `results/` directory.

---

## 🚀 Quantitative Research Perspective

This framework is relevant to quantitative finance and HFT:

- First-passage times for barrier crossings,
- Liquidity flow in order-book networks,
- Risk propagation in correlation graphs,
- Spectral properties of the Laplacian related to mixing and stability.

The project demonstrates the ability to translate stochastic systems into
deterministic representations — a core quantitative research skill.

---

## ▶️ How to Run

```bash
pip install networkx numpy matplotlib
python the_resistance_of_randomness.py
