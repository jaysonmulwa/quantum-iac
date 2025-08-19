import yaml
import subprocess

class Transpiler():
    def __init__(self, circuit_file):
        self.circuit_name = ""
        self.engine = ""
        self.qubits = 0
        self.transform_list = []
        self.circuit_file = circuit_file
        self.parsed_yaml = {}
        self.output_file = "./output.py"

    def run_file(self):
        subprocess.run(["python", self.output_file])
        

    def prepare_output_file(self):

        open(self.output_file, "w").close()
        
        lines = ["import numpy as np", "from qiskit import QuantumCircuit", f"qc = QuantumCircuit({self.qubits})"]
        with open(self.output_file, "a") as f:
            f.writelines(line + "\n" for line in lines)

    def to_qiskit(self):
        print(self.transform_list)
        for transform in self.transform_list:
            gate_name = transform['name']
            targets = transform['targets']

            _command = ""
            match(gate_name):
                case "hadamard":
                    _command = f"qc.h({targets[0]})"
                case "phase":
                    _command = f"qc.p({targets[0]}, {targets[1]})" 
                case "cnot":
                    _command = f"qc.cx({targets[0]}, {targets[1]})"

            # append to a newly created yml file
            with open(self.output_file, "a") as f:
                f.write(_command + "\n")
        
        with open(self.output_file, "a") as f:
                f.write("print(qc)" + "\n")

    def parse_yml(self):
        # Load the YAML
        with open(self.circuit_file, "r") as f:
            data = yaml.safe_load(f)

        self.parsed_yaml = data
        self.circuit_name = data.get("circuit_name")
        self.engine = data.get("engine")
        self.qubits = data.get("qubits")

        for step in data.get("transform", []):
            gate_name = step.get("name")
            gate_targets = step.get("targets")

            if gate_name and gate_targets:
                self.transform_list.append({'name': gate_name, "targets": gate_targets})
                print(f"  - Gate: {gate_name}, Params: {gate_targets}")
                

    def init(self):
        self.parse_yml()
        self.prepare_output_file()
        self.to_qiskit()
        self.run_file()


transpiler = Transpiler(circuit_file="circuit.yml")
transpiler.init()