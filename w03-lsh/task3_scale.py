#!/usr/bin/env python3
"""Week 3 · Task 3 — Find the same pairs without comparing everything.

Textbook §3.4.

`BruteForce` compares every pair. On 3,000 documents that is 4.5 million
comparisons and it is completely correct. On 3 million documents it is 4.5
trillion and it is completely useless.

Beat it. Find the same near-duplicate pairs while making far fewer comparisons.

    python3 bench.py
    python3 bench.py --yours

The harness counts every call you make to `similarity()`. That is your score.
It also checks **recall** - which of the truly similar pairs you found. Skipping
comparisons is easy; skipping comparisons without losing the pairs is the task.
"""


class BruteForce:
    """Correct, and quadratic."""

    def __init__(self, threshold):
        self.threshold = threshold

    def find(self, docs, similarity):
        """docs is [set_of_shingles, ...]. Return {(i, j), ...} with i < j."""
        out = set()
        for i in range(len(docs)):
            for j in range(i + 1, len(docs)):
                if similarity(docs[i], docs[j]) >= self.threshold:
                    out.add((i, j))
        return out


class YourFinder:
    """Your near-duplicate finder.

        __init__(threshold)
        find(docs, similarity) -> {(i, j), ...}

    `similarity(a, b)` is the only way to compare two documents, and every call
    is counted. Everything else - signatures, banding, bucketing - is free, in
    the sense that the harness does not charge you for it. That is deliberate:
    it is also roughly true at scale, where the comparison is the expensive
    part and the hashing is linear.

    Two knobs decide everything:

        the number of hashes in a signature
        how many bands you split it into

    §3.4.2 gives you the relationship between those and the probability that a
    pair at similarity s becomes a candidate. It is an S-curve, and where its
    step sits is something you choose. Choose it on purpose and be able to say
    why in observation.md - a threshold of 0.8 does not mean bands should be
    anything in particular until you have done the arithmetic.

    You may reuse your Task 1 code.
    """

    def __init__(self, threshold):
        self.threshold = threshold
        self.num_hashes = 120
        self.bands = 30
        self.rows_per_band = self.num_hashes // self.bands

    def find(self, docs, similarity):
        # A prime larger than all shingle values
        prime = 10007

        # Create deterministic hash functions
        hash_params = []
        for i in range(self.num_hashes):
            a = 2 * i + 1
            b = 3 * i + 7
            hash_params.append((a, b))

        # Build MinHash signatures
        signatures = []

        for doc in docs:
            sig = []

            for a, b in hash_params:
                minimum = min(
                    ((a * x + b) % prime)
                    for x in doc
                )
                sig.append(minimum)

            signatures.append(sig)

        # LSH banding
        candidates = set()

        for band in range(self.bands):
            buckets = {}

            start = band * self.rows_per_band
            end = start + self.rows_per_band

            for i, sig in enumerate(signatures):
                key = tuple(sig[start:end])

                if key not in buckets:
                    buckets[key] = []

                buckets[key].append(i)

            # Every pair in the same bucket becomes a candidate
            for bucket in buckets.values():
                for x in range(len(bucket)):
                    for y in range(x + 1, len(bucket)):
                        candidates.add((bucket[x], bucket[y]))

        # Only perform the expensive real comparison on candidates
        result = set()

        for i, j in candidates:
            if similarity(docs[i], docs[j]) >= self.threshold:
                result.add((i, j))

        return result
