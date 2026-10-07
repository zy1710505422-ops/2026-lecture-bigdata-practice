# Task 2: Memory Limits

## Machine

- CPU: Intel Core i9-13900H
- RAM: 16 GB
- OS: Windows 11
- Python: 3.14.7
- Other applications: Google Chrome, VS Code and Task Manager.
- Available RAM before the additional tests was about 3.9 GB.

## Measurements

Memory is reported in decimal MB. FM ratio means estimate / true distinct count.

| Stream size | True distinct | Exact time (s) | Exact peak (MB) | FM time (s) | FM peak (MB) | FM ratio |
|---:|---:|---:|---:|---:|---:|---:|
| 25,000 | 9,189 | 0.08 | 0.977 | 52.00 | 0.005538 | 0.932 |
| 100,000 | 36,702 | 0.29 | 3.925 | 184.69 | 0.004252 | 1.110 |
| 400,000 | 146,970 | 1.27 | 11.591 | 1,636.79 | 0.004098 | 1.266 |
| 1,600,000 | 587,625 | 5.69 | 46.647 | 15,504.48 | 0.004042 | 0.940 |

The 25,000-item run used an optimized FM implementation. It produces the same hashes and uses the same combining rule, but has additional fixed-size working arrays. Its time and memory are therefore not directly comparable to the earlier implementation.

## Additional Exact-Only Tests

| Stream size | True distinct | Exact time (s) | Exact peak (MB) |
|---:|---:|---:|---:|
| 25,000,000 | 9,179,304 | 158.12 | 744.84 |
| 50,000,000 | 18,358,721 | 175.61 | 1,499.78 |

These additional tests did not run FM. Their outputs are saved in exact_limit.txt and exact_limit_50m.txt.

## Practical Limit

I stopped at 50,000,000 items. The exact method still completed, taking 175.61 seconds and about 1.5 GB of traced peak memory.
At 25,000,000 items, I noticed a brief pause of about one second.
I did not observe an out-of-memory failure or establish an unbearable size. The exact limit remains beyond what I tested, so requirement A2 is not fully demonstrated.

## Memory Growth

The exact set stores all distinct values, so its memory grows approximately linearly with the number of distinct items.
For this generator, distinct count grows approximately proportionally to n, giving roughly O(n) memory when treating each key as a fixed-size item.
Doubling n from 25 million to 50 million increased peak memory from 744.84 MB to 1,499.78 MB, about 2.01 times.

FM stores a fixed number of maxima and working values. Its memory is O(n_hashes), or O(1) relative to stream length when n_hashes is fixed at 64.
The original implementation used about 4 KB at all three sizes. The optimized implementation used about 5.5 KB.

These memory figures are measured by tracemalloc, not total process RAM. The printed 0.00 MB for some FM runs is rounding, not zero memory usage.

## Accuracy

FM ratios were 0.932, 1.110, 1.266 and 0.940 in increasing order of stream size.
Accuracy did not consistently improve or worsen as n increased.
All four estimates were within a factor of two of the true distinct count.