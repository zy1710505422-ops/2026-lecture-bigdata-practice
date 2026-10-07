# Observations

## Task 1
Bloom filters cannot have false negatives because insertion sets every bit checked by lookup, and those bits are never cleared; predicted false positives were 0.860%, compared with 0.890% measured, with the small difference consistent with sampling variation.
For FM, I averaged R within groups, converted each group to 2^mean(R), then took the median; the estimate was 23,519 versus 19,953 true distinct items. Direct averaging of 2^R is sensitive to outliers; I did not separately measure alternative combining rules.
Reservoir sampling uses rng.randrange(n) and replaces an item only when position < k, giving each incoming item probability k/n without knowing the final stream length and retaining at most k items.

## Task 2
I stopped at 50 million items: exact counting took 175.61 seconds and 1,499.78 MB, but still completed, so I did not establish a failure or unbearable size.
Exact memory grows roughly O(n) for this data, while FM uses O(n_hashes), constant relative to n with 64 hashes.
A factor-of-two estimate can be acceptable for a rough traffic overview, but is too inaccurate for precise visitor reporting or decisions involving small changes.

## Task 3
I changed the number of hashes from 1 to 7: minimizing p = (1 - exp(-kn/m))^k gives k = (m/n) ln(2), and 10 ln(2) is about 6.93.
The optimal Bloom-filter prediction for 10 bits per item is about 0.819%; my measured rate was 0.7995%, with zero false negatives, close to the prediction. A finite measurement can fall slightly below the theoretical prediction.
If n were unknown, I would use a scalable Bloom filter that adds filters as capacity is reached, allowing more memory; underestimating n raises false positives, while overestimating n wastes memory.