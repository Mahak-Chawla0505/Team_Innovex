
import json
from backend.utils import process_entry

def run_case(file_path):
    print(f"\nRunning: {file_path}\n")

    with open(file_path, "r", encoding="utf-8") as f:
        timeline = json.load(f)

    history = []

    for entry in timeline:
        result = process_entry(entry["text"], history)

        print(f"Day {entry['day']}: {result['label']} | Spiral: {result['spiral']}")


run_case("data/spiral_case.json")
run_case("data/normal_case.json")
run_case("data/positive_case.json")