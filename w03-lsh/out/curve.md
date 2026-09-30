# Task 2 Timing Curve

| n | Brute Force Time (s) | LSH Time (s) | Brute Comparisons | LSH Comparisons |
|---|---:|---:|---:|---:|
| 250 | 0.35 | 1.39 | 31,125 | 23 |
| 500 | 1.27 | 2.45 | 124,750 | 126 |
| 1000 | 8.58 | 8.85 | 499,500 | 514 |
| 2000 | 18.95 | 9.48 | 1,999,000 | 1,777 |

The crossover occurred between n = 1000 and n = 2000. At n = 1000, brute force was slightly faster, but at n = 2000, LSH was clearly faster.

The brute-force comparison count grows quadratically. Doubling n from 250 to 500 increased comparisons from 31,125 to 124,750, which is about 4x. Doubling from 500 to 1000 increased comparisons to 499,500, again about 4x.

LSH is slower at small n because it has preprocessing costs, including computing MinHash signatures, splitting them into bands, and building hash buckets before performing similarity comparisons.

At n = 2000, brute force took 18.95 seconds while LSH took 9.48 seconds. This was the point where brute force became noticeably unpleasant on my machine.

The requested tests at n = 4000 and n = 8000 were also run, but the benchmark generator only provides 2,120 documents, so those runs reused the full available dataset instead of actually testing 4,000 or 8,000 documents.