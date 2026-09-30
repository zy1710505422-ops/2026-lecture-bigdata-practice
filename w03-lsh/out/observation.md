## Task 1
I used one pass over the rows so the matrix does not need to be scanned separately for every document. If the signature length is not divisible by the number of bands, my code raises an error. Using more hash functions would make the MinHash estimate closer to the true Jaccard similarity, but it would require more computation and memory.

## Task 2
The crossover on my machine occurred between n = 1000 and n = 2000. The brute-force comparison count grew by about 4x when n doubled, which matches quadratic growth. Around n = 2000, brute force became noticeably slow, while LSH was already faster.

## Task 3
I used 120 hash values and 30 bands, so each band has 4 rows. The S-curve step is approximately (1/30)^(1/4) = 0.427, which is below the threshold 0.6 and helps preserve recall. The result achieved 100% recall while avoiding 99.91% of similarity comparisons.python bench.py --yours > out/bench.txt