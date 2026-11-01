"""
Load or generate RNA sequences and enumerate valid candidate base pairs.

TODO:
- load_sequence(path_or_string) -> the RNA sequence as a string of A/U/G/C
- generate_synthetic_sequence(length, seed) -> a random short sequence for testing
- enumerate_valid_pairs(sequence, allow_wobble=True) -> list of (i, j) index pairs that are
  chemically valid (A-U, G-C, optionally G-U)
"""
