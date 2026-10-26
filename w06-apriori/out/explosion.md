# Task 2 — Support Threshold Explosion

## Experimental Results

| Support | Frequent Pairs | Peak Counters | Peak Memory (MB) |
|---|---:|---:|---:|
| 400 | 249 | 10,585 | 1.1 |
| 200 | 776 | 58,626 | 6.7 |
| 100 | 2,244 | 273,701 | 28.6 |
| 50 | 6,397 | 820,259 | 107.7 |
| 25 | 17,045 | 893,456 | 107.7 |
| 12 | 43,116 | 893,456 | 110.0 |
| 6 | 101,938 | 893,456 | 126.5 |
| 3 | 250,054 | 893,456 | 163.9 |
| 2 | 424,620 | 893,456 | 212.0 |
| 1 | 893,456 | 893,456 | 334.2 |

## A2 — Machine Limit

All tested thresholds completed successfully. Support 1 was the lowest possible positive threshold and produced the highest measured memory usage (334.2 MB). No failure or severe slowdown occurred.

## A4 — Counter Growth

When support decreased from 400 to 200, peak counters increased by approximately 5.54 times. From 200 to 100, they increased by 4.67 times. The growth was initially much faster than doubling, but reached a plateau of 893,456 counters at support 25.

## A5 — Frequent Pairs vs. Counters

Frequent pairs increased from 249 to 893,456 as support decreased from 400 to 1. Peak counters reached 893,456 at support 25 and stayed constant, while the number of frequent pairs continued to increase. This gap shows that many candidate pairs must be counted even when relatively few satisfy the support threshold.

## A6 — Machine Environment
- Operating system: Windows
- CPU: AMD Ryzen 7 9700X 8-Core Processor
- CPU cores: 8 cores, 16 logical processors
- RAM: 32 GB DDR5 (6000 MT/s)
- Other running applications: VS Code, PowerShell, and Windows background processes
- Memory usage during experiment: Up to 334.2 MB (tracemalloc)