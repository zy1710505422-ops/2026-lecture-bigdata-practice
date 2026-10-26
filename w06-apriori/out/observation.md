# Week 6 Lab — Observations

## Task 1 — A-Priori and Association Rules

Confidence is directional. In the supplied baskets, diaper → beer and beer → diaper both have confidence 0.80 because each item appears in five baskets. Both rules have lift 1.12, indicating only a weak positive association.

The highest confidence is 0.80, shared by several rules, including diaper → beer. Its lift is only 1.12, so the relationship is not particularly convincing.

For 2,000 items, brute force requires 1,999,000 possible pair counters. In the seven-basket example, Apriori reduces the candidates to 6 after pass one. This is a small illustrative dataset, not the 2,000-item benchmark.

## Task 2 — Threshold Explosion

All ten thresholds completed successfully, including support 1, which used 334.2 MB of measured peak Python memory. No threshold became unbearable; support 1 was the lowest meaningful positive threshold.

Peak counters increased 5.54× when support fell from 400 to 200 and 4.67× from 200 to 100, before reaching 893,456 at support 25.

Frequent pairs grew from 249 at support 400 to 893,456 at support 1. The counter count reached its maximum much earlier than the answer count, showing that many candidates must be tracked even when only a small fraction are frequent.

## Task 3 — PCY Optimization

I used 1,000,003 hash buckets. With support 50, PCY reduced peak pair counters from 820,259 to 13,168, a 98.4% reduction, while finding exactly the same 6,397 frequent pairs.

The bucket array itself requires approximately 1,000,003 integer slots during pass one, so a reduction in pair counters does not automatically mean a reduction in total peak memory. PCY becomes advantageous when the memory saved by filtering candidate pairs exceeds the bucket-array overhead. The crossover depends on the number of candidates, bucket size, collision rate, and data distribution.

Reducing the bucket count to 100,003 increased peak pair counters to 148,595, giving only an 81.9% reduction. Smaller bucket arrays save space during pass one but cause more hash collisions and more candidate counters during pass two.