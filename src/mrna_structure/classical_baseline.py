"""
Classical folding baseline — the ground truth the quantum solver is compared against.

TODO:
- nussinov_fold(sequence) -> the optimal non-crossing base-pairing structure + its score,
  via classical dynamic programming
- structure_to_pairs(structure) -> convert a dot-bracket or matrix representation to a list
  of (i, j) pairs, for comparison with the quantum solver's output
"""
