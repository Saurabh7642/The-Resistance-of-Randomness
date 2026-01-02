import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

# 1. GRAPH SETUP

G = nx.Graph()

edges = [
    ('U', 'A'), ('U', 'E'), ('A', 'B'), ('A', 'F'),
    ('B', 'D'), ('D', 'K'), ('D', 'V'),
    ('E', 'F'), ('E', 'V'), ('F', 'V')
]

G.add_edges_from(edges)

u, v = 'U', 'V'
m = G.number_of_edges()   # number of edges


# 2. RANDOM WALK SIMULATION (HITTING TIMES)
def get_hitting_time(graph, start, target):
    current = start
    steps = 0
    while current != target:
        neighbors = list(graph.neighbors(current))
        current = random.choice(neighbors)
        steps += 1
    return steps


trials = 10000
h_uv = []
h_vu = []

for _ in range(trials):
    h_uv.append(get_hitting_time(G, u, v))
    h_vu.append(get_hitting_time(G, v, u))

avg_h_uv = np.mean(h_uv)
avg_h_vu = np.mean(h_vu)
simulated_commute = avg_h_uv + avg_h_vu

# 3. THEORETICAL COMPUTATION (EFFECTIVE RESISTANCE)
L = nx.laplacian_matrix(G).toarray()
nodes = list(G.nodes())

u_idx = nodes.index(u)
v_idx = nodes.index(v)

# Ground node v (remove row & column)
L_reduced = np.delete(np.delete(L, v_idx, axis=0), v_idx, axis=1)

b = np.zeros(len(nodes) - 1)
new_u_idx = u_idx if u_idx < v_idx else u_idx - 1
b[new_u_idx] = 1     # Inject 1A at node U

voltages = np.linalg.solve(L_reduced, b)
R_uv = voltages[new_u_idx]

theoretical_commute = 2 * m * R_uv


# 4. RESULT
print("----- SIMULATION RESULTS -----")
print(f"Average H_uv (U → V): {avg_h_uv:.2f}")
print(f"Average H_vu (V → U): {avg_h_vu:.2f}")
print(f"Simulated Commute Time: {simulated_commute:.2f}")

print("\n----- THEORETICAL RESULTS -----")
print(f"Effective Resistance R_uv: {R_uv:.4f}")
print(f"Theoretical Commute Time (2mR): {theoretical_commute:.2f}")


# 5. DISTRIBUTION PLOT
plt.figure(figsize=(10, 6))
plt.hist(h_uv, bins=range(0, 110, 3), alpha=0.5, label='U → V')
plt.hist(h_vu, bins=range(0, 110, 3), alpha=0.5, label='V → U')
plt.xlabel("Number of Steps")
plt.ylabel("Frequency")
plt.title("Distribution of Random Walk Hitting Times")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
