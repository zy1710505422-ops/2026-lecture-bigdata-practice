# Week 5 Lab — Observations

## Task 1: PageRank and Its Failures

In the broken version, rank entering a dead end disappears because the node has no outgoing links. I fixed this by distributing its rank uniformly across all nodes.

Teleportation fixes both dead ends and spider traps by allowing the surfer to move to any page. Beta represents the probability of following a link, while 1 - beta is the probability of randomly jumping to another page.

## Task 2: PageRank Convergence

As beta increases from 0.50 to 0.99, iterations increase from 14 to 24 because less teleportation slows convergence.

Increasing graph size from 1,200 to 20,000 barely changes the iteration count (20 to 21 at beta = 0.85), but greatly increases execution time because each iteration processes more nodes and edges.

The top-10 ranking changes at beta = 0.70, showing that published rankings can depend on the chosen beta value.

## Task 3: Sparse PageRank

Instead of storing an n × n matrix, I used the adjacency list and two rank vectors, requiring approximately 2n rank floats rather than n² matrix floats.

Teleportation and dead-end redistribution only require adding the same base value to each node, without creating a dense matrix.

The worst per-node difference was 1.18e-15, caused by floating-point rounding and different summation orders rather than an algorithmic error.
## Task 4: Optional Spark PageRank

I implemented the local PageRank version by reusing the sparse algorithm from Task 3.

At 50,000 nodes and 376,379 edges, the single-process version finished in 3.59 seconds with 19.3 MB peak memory. The top-ranked node was 147.

The Spark comparison was not executed because Java and PySpark were not installed.

The provided Spark implementation does not redistribute rank from dead ends, so rank mass can be lost. Spark also introduces distributed processing overhead, but it can handle larger graphs by distributing data across workers.