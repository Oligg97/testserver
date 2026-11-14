import json
from pathlib import Path

from SE1 import SE1
from SE2 import SE2
from SE3 import SE3

# test the functions with sample inputs
test1 = SE1(movement=1, noise=1)
test2 = SE2(fald=1, stod=0)
test3 = SE3(sleep=0, wake=1)

results = [
    {
        "id": "test1",
        "sensor": "SE1",
        "inputs": {"movement": 1, "noise": 1},
        "result": test1,
    },
    {
        "id": "test2",
        "sensor": "SE2",
        "inputs": {"fald": 1, "stod": 0},
        "result": test2,
    },
    {
        "id": "test3",
        "sensor": "SE3",
        "inputs": {"sleep": 0, "wake": 1},
        "result": test3,
    },
]

output_file = Path(__file__).with_name("results.json")
output_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
print(f"JSON data gemt i {output_file.name}")

