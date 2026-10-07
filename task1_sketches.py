#!/usr/bin/env python3
"""Week 4 · Task 1 — Answer questions about a stream you cannot store.

Textbook §4.3 (sampling), §4.4 (Bloom filter), §4.5 (Flajolet-Martin).

The premise of the whole chapter: the stream is longer than your memory, it
goes past once, and you still have to answer. Every method here trades an exact
answer for a bounded amount of space, and the job is to know exactly what you
traded.

You build three, and the harness checks each against the truth it is
approximating.

    python3 task1_sketches.py --verify
"""
import argparse, random

def hash64(item, seed, index):
    mask = (1 << 64) - 1
    value = 14695981039346656037

    for byte in str(item).encode("utf-8"):
        value = ((value ^ byte) * 1099511628211) & mask

    value = (value + seed + (index + 1) * 0x9E3779B97F4A7C15) & mask
    value = ((value ^ (value >> 30)) * 0xBF58476D1CE4E5B9) & mask
    value = ((value ^ (value >> 27)) * 0x94D049BB133111EB) & mask
    return value ^ (value >> 31)
class BloomFilter:


    def __init__(self, m, k, seed=246):
        self.m = m
        self.k = k
        self.seed = seed
        self.bits = bytearray((m + 7) // 8)

    def add(self, item):
        for i in range(self.k):
            position = hash64(item, self.seed, i) % self.m
            self.bits[position // 8] |= 1 << (position % 8)
    def __contains__(self, item):
        for i in range(self.k):
            position = hash64(item, self.seed, i) % self.m
            if not (self.bits[position // 8] & (1 << (position % 8))):
                return False
        return True

    def expected_fp_rate(self, n_inserted):
        return (1 - 2.718281828459045 ** (
            -self.k * n_inserted / self.m
        )) ** self.k

def flajolet_martin(stream, n_hashes=64, seed=246):
        maxima = [0] * n_hashes
        seen_any = False

        mask = (1 << 64) - 1
        offsets = [
        (seed + (i + 1) * 0x9E3779B97F4A7C15) & mask
        for i in range(n_hashes)
    ]
        thresholds = [(1 << (r + 1)) - 1 for r in maxima]

        for item in stream:
         seen_any = True
         base = 14695981039346656037

         for byte in str(item).encode("utf-8"):
            base = ((base ^ byte) * 1099511628211) & mask

         for i in range(n_hashes):
            value = (base + offsets[i]) & mask
            value = ((value ^ (value >> 30)) * 0xBF58476D1CE4E5B9) & mask
            value = ((value ^ (value >> 27)) * 0x94D049BB133111EB) & mask
            value ^= value >> 31

            if value & thresholds[i] == 0:
                zeros = (value & -value).bit_length() - 1 if value else 64
                maxima[i] = zeros
                thresholds[i] = (1 << (zeros + 1)) - 1

        if not seen_any:
          return 0.0

        group_size = max(1, int(n_hashes ** 0.5))
        estimates = []

        for start in range(0, n_hashes, group_size):
         group = maxima[start:start + group_size]
         estimates.append(2.0 ** (sum(group) / len(group)))

        estimates.sort()
        middle = len(estimates) // 2

        if len(estimates) % 2:
         return estimates[middle]
        return (estimates[middle - 1] + estimates[middle]) / 2


def reservoir_sample(stream, k, seed=246):
        if k <= 0:
         return []

        rng = random.Random(seed)
        sample = []

        for n, item in enumerate(stream, start=1):
         if n <= k:
            sample.append(item)
         else:
            position = rng.randrange(n)
            if position < k:
                sample[position] = item

        return sample


# ------------------------------------------------------------------- harness
def verify():
    fails = 0
    rng = random.Random(246)

    def check(label, ok, detail=""):
        nonlocal fails
        print(f"  {'ok  ' if ok else 'FAIL'}  {label:<46} {detail}")
        fails += not ok

    # --- Bloom: no false negatives, ever
    try:
        bf = BloomFilter(m=8192, k=5)
    except NotImplementedError:
        print("  BloomFilter is still a stub"); return 1
    inserted = [f"item-{i}" for i in range(800)]
    for x in inserted:
        bf.add(x)
    check("no false negatives", all(x in bf for x in inserted))

    absent = [f"other-{i}" for i in range(20_000)]
    fp = sum(1 for x in absent if x in bf) / len(absent)
    predicted = bf.expected_fp_rate(len(inserted))
    close = abs(fp - predicted) < max(0.02, predicted * 0.5)
    check("measured false-positive rate matches theory", close,
          f"measured {fp:.3%}, predicted {predicted:.3%}")

    # --- Flajolet-Martin: a factor of two is what this method gives you
    try:
        distinct = 20_000
        stream = [f"k{rng.randrange(distinct)}" for _ in range(120_000)]
        est = flajolet_martin(stream)
    except NotImplementedError:
        print("  flajolet_martin is still a stub"); return 1
    true_distinct = len(set(stream))
    ratio = est / true_distinct
    check("distinct estimate within a factor of 2", 0.5 <= ratio <= 2.0,
          f"estimated {est:,.0f}, true {true_distinct:,} ({ratio:.2f}x)")

    # --- Reservoir: uniform over many trials
    try:
        counts = [0] * 20
        trials = 4000
        for t in range(trials):
            s = reservoir_sample(range(20), 5, seed=t)
            for i in s:
                counts[i] += 1
    except NotImplementedError:
        print("  reservoir_sample is still a stub"); return 1
    expected = trials * 5 / 20
    spread = (max(counts) - min(counts)) / expected
    check("reservoir is uniform across items", spread < 0.15,
          f"spread {spread:.1%} around {expected:.0f}")

    print(f"\n  {'all ok' if not fails else str(fails) + ' failed'}")
    return 1 if fails else 0


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--verify", action="store_true")
    a = p.parse_args()
    raise SystemExit(verify() if a.verify else p.print_help())
