"""
Run the folding Hamiltonian through a variational quantum algorithm.

TODO:
- build_ansatz(num_qubits, reps) -> the parameterized circuit
- run_cvar_vqe(hamiltonian, ansatz, optimizer, alpha) -> solution + energy, using a
  CVaR-based objective (as in the IBM/Moderna approach) rather than plain expectation value
"""
