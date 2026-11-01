"""
Build the Hamiltonian / QUBO encoding the folding objective and constraints.

TODO:
- build_folding_hamiltonian(sequence, valid_pairs, penalty_weights) -> Hamiltonian/QUBO
  rewarding valid, non-crossing, energy-favorable pairings and penalizing violations
  (a base pairing more than once, crossing pairs)
- decode_solution(bitstring, valid_pairs) -> the predicted structure as a list of pairs
"""
