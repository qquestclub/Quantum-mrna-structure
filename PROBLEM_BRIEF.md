# Problem Brief: mRNA Secondary Structure Prediction

## Background

An mRNA molecule's secondary structure — which bases fold back and pair with which other
bases — affects its stability and how well it's translated into protein, which matters a lot
for mRNA vaccine and therapeutic design. Predicting the lowest-free-energy folding of a
sequence is a combinatorial optimization problem: choose a set of non-crossing base pairs that
minimizes total folding energy. IBM has published work with Moderna exploring variational
quantum algorithms (VQAs), specifically CVaR-based VQE, for exactly this problem.

## Objective

Given a short RNA sequence (start with 10–20 bases, synthetic or from a public dataset), find
the base-pairing configuration that minimizes an approximate free-energy objective, subject to:

- **Validity constraints**: only complementary bases (A–U, G–C, and optionally G–U wobble
  pairs) can pair
- **Non-crossing constraint**: base pairs can't "cross" each other (standard secondary
  structure — no pseudoknots, at least for the base version of this challenge)
- Each base pairs with at most one other base

## Deliverables

1. **Problem formulation** — the folding objective + constraints written as a QUBO/Ising
   Hamiltonian (or a CVaR-based cost function for VQE), documented in `docs/`.
2. **Classical baseline** — a classical dynamic-programming folding algorithm (e.g. Nussinov's
   algorithm), used as ground truth for small sequences.
3. **Quantum/hybrid solver** — a variational quantum algorithm (VQE with a CVaR-based
   objective, as in the IBM/Moderna approach) solving the same instance.
4. **Benchmark report** — how close the predicted structure gets to the classical
   ground-truth structure, and runtime, across at least 3 sequence lengths.
5. **5–10 minute pitch** — for the Nov 5 demo day: the real-world problem, your formulation,
   what you found, and where quantum struggled to keep up as sequences got longer.

## Evaluation criteria

- Correctness of the formulation (only valid, non-crossing pairs actually encoded)
- Rigor of the classical baseline (a real folding algorithm, not a guess)
- Honesty in the benchmark, especially about how quickly this becomes intractable to simulate
- Clarity of the final pitch

## Suggested approach

1. Implement Nussinov's algorithm classically first — this gives you ground truth and forces
   you to understand the problem before touching quantum.
2. Encode a tiny 6–10 base synthetic sequence as a QUBO by hand, verify against Nussinov.
3. Read the IBM/Moderna CVaR-VQE approach before designing your own variational ansatz —
   don't reinvent the cost function from scratch.
4. Scale sequence length gradually; note the point where your simulator becomes too slow.

## Real-world grounding

See `docs/references.md` for the IBM–Moderna collaboration this challenge is drawn from.
