# Task 2 — PageRank Convergence Analysis

## A1–A3: Beta and Convergence

| Beta | Nodes | Iterations | Time (s) |
|---|---|---|---|
| 0.50 | 1200 | 14 | 0.065 |
| 0.70 | 1200 | 17 | 0.050 |
| 0.85 | 1200 | 20 | 0.052 |
| 0.95 | 1200 | 23 | 0.064 |
| 0.99 | 1200 | 24 | 0.058 |

As beta approaches 1, the number of iterations increases from 14 to 24. This happens because the probability of teleportation decreases, making convergence slower.

## A4: Graph Size

| Nodes | Beta | Iterations | Time (s) |
|---|---|---|---|
| 1200 | 0.85 | 20 | 0.052 |
| 20000 | 0.85 | 21 | 1.110 |
| 1200 | 0.95 | 23 | 0.064 |
| 20000 | 0.95 | 24 | 1.289 |

Increasing graph size from 1,200 to 20,000 nodes barely changes the iteration count, but significantly increases execution time. Larger graphs require more computation per iteration, while the convergence rate depends mainly on the graph structure, beta, and tolerance.

## A5: Tolerance

| Tolerance | Beta | Iterations | Time (s) |
|---|---|---|---|
| 1e-6 | 0.85 | 12 | 0.025 |
| 1e-10 | 0.85 | 20 | 0.052 |

Making the tolerance four decimal orders stricter requires 8 additional iterations, approximately 2 iterations per extra decimal digit in this experiment.

## A6: Top-10 Ranking

The top-10 ranking first changes at beta = 0.70 compared with beta = 0.50. Nodes p00000 and p00004 switch positions (7th and 8th). The top three nodes remain unchanged across all tested beta values.

This shows that the choice of beta can influence published rankings, even when the highest-ranked pages remain stable.

## A7: Machine Information

- Operating system: Windows 11
- CPU: 13th Gen Intel Core i9-13900H
- RAM: 16 GB DDR4
- Python version: 3.14.7
- Other running applications: VS Code, PowerShell, Windows Task Manager, and web browser.