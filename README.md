# QFF Industry Challenge — mRNA Secondary Structure Prediction

Team project for the Qiskit Fall Fest 2026 Industry Challenge track (QQuest, MIT ADT University).
Inspired by IBM's published collaboration with Moderna on using variational quantum algorithms
for mRNA secondary structure prediction — read [`PROBLEM_BRIEF.md`](./PROBLEM_BRIEF.md) first.

## Goal

Formulate mRNA secondary structure prediction (which bases pair with which, folding the
sequence to minimize free energy) as a combinatorial optimization problem, solve it with a
variational quantum algorithm, and benchmark against a classical folding baseline.

## Repo structure

```
qff-challenge-mrna-structure/
├── PROBLEM_BRIEF.md              # the challenge statement — read this first
├── data/
│   ├── raw/                      # original RNA sequences (FASTA files etc.), untouched
│   └── processed/                # cleaned sequences, precomputed base-pairing candidates
├── notebooks/                    # exploratory work — one notebook per question, numbered
├── src/mrna_structure/
│   ├── data_loader.py            # load RNA sequences, generate valid base-pair candidates
│   ├── classical_baseline.py     # classical folding algorithm (e.g. Nussinov) — the benchmark
│   ├── hamiltonian_formulation.py# build the Hamiltonian/QUBO encoding the folding objective
│   ├── vqa_solver.py             # run a variational quantum algorithm (CVaR-VQE style)
│   ├── benchmark.py              # compare predicted structures + runtime across solvers
│   └── utils.py                  # shared helpers
├── tests/                        # unit tests for src/
├── results/                      # predicted structures, benchmark tables, plots
└── docs/references.md            # papers & industry pilots this project is grounded in
```

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Then work through `notebooks/01_sequence_exploration.ipynb` (create this first) before writing
anything in `src/`.

## Team workflow

- One branch per person/pair, PR into `main`.
- Land the classical baseline (`classical_baseline.py`) before touching the quantum solver —
  you need a known-correct structure to compare against.
- Start with a very short synthetic RNA sequence (10–20 bases) before touching anything
  biologically real — this problem gets hard fast.

## Status

🚧 Skeleton only — no logic implemented yet. See TODOs in each file under `src/`.
