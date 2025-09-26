# Quantum Infrastructure as Code
Quantum Circuits as Infra

We try out a little experiment where Quantum Circuits can be declared imperatively, and the sequence of operations on the circuit declared.

The output is a Python Qiskit file, which is generated from parsing the circuit .yaml file.

On top of providing us with a standard way to declare quantum circuits (perhaps beyond the scope of Qiskit); 

We also get interesting use cases for the .yml declaration files:
- Comparing multiple .yml files.
- Setting rules for linting before execution.
- Documenting circuit changes more concisely.


# Roadmap

- [x] Parse simple circuit definition as yml and convert to Python.
- [x] Directly execute resultant .py file.
- [ ] Characterize Quantum circuits from their graph-like properties.
- [ ] Compare multiple .yml file/ document state changes between versions.
- [ ] Circuit manager - to treat circuits as inventory.
- [ ] Be able to swap out engines e.g. Qiskit vs Cirq.
