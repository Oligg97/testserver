import json
from datetime import datetime
from pathlib import Path

from SE1 import SE1
from SE2 import SE2
from SE3 import SE3

# test the functions with sample inputs
test1_inputs = {"movement": 1, "noise": 1}
test1 = SE1(**test1_inputs)  # Pakker inputfelterne ud som navngivne argumenter.
test2_inputs = {"fald": 0, "stod": 1}
test2 = SE2(**test2_inputs)
test3_inputs = {"sleep": 1, "wake": 0}
test3 = SE3(**test3_inputs)

timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

results = [
    {
        "id": "test1",
        "sensor": "SE1",
        "inputs": test1_inputs,
        "result": test1,
        "timestamp": timestamp,
    },
    {
        "id": "test2",
        "sensor": "SE2",
        "inputs": test2_inputs,
        "result": test2,
        "timestamp": timestamp,
    },
    {
        "id": "test3",
        "sensor": "SE3",
        "inputs": test3_inputs,
        "result": test3,
        "timestamp": timestamp,
    },
]

output_file = Path(__file__).with_name("results.json")
output_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
print(f"JSON data gemt i {output_file.name}")

