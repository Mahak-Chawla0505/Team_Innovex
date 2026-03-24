import json
import random

# Load your dataset
with open("data/sample_entries.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Separate by sentiment
positive = [d for d in data if d["label"] == "POSITIVE"]
negative = [d for d in data if d["label"] == "NEGATIVE"]
neutral = [d for d in data if d["label"] == "NEUTRAL"]

# Safety fallback
if not neutral:
    neutral = positive

# -----------------------------
# 1. SPIRAL CASE (declining mood)
# -----------------------------
spiral_case = [
    {"day": 1, "text": random.choice(positive)["text"]},
    {"day": 2, "text": random.choice(neutral)["text"]},
    {"day": 3, "text": random.choice(negative)["text"]},
    {"day": 4, "text": random.choice(negative)["text"]},
    {"day": 5, "text": random.choice(negative)["text"]},
]

# -----------------------------
# 2. NORMAL CASE (fluctuating mood)
# -----------------------------
normal_case = [
    {"day": 1, "text": random.choice(positive)["text"]},
    {"day": 2, "text": random.choice(negative)["text"]},
    {"day": 3, "text": random.choice(positive)["text"]},
    {"day": 4, "text": random.choice(neutral)["text"]},
    {"day": 5, "text": random.choice(negative)["text"]},
]

# -----------------------------
# 3. POSITIVE CASE (stable mood)
# -----------------------------
positive_case = [
    {"day": 1, "text": random.choice(positive)["text"]},
    {"day": 2, "text": random.choice(positive)["text"]},
    {"day": 3, "text": random.choice(positive)["text"]},
    {"day": 4, "text": random.choice(positive)["text"]},
    {"day": 5, "text": random.choice(positive)["text"]},
]

# -----------------------------
# SAVE FILES
# -----------------------------
with open("data/spiral_case.json", "w", encoding="utf-8") as f:
    json.dump(spiral_case, f, indent=4)

with open("data/normal_case.json", "w", encoding="utf-8") as f:
    json.dump(normal_case, f, indent=4)

with open("data/positive_case.json", "w", encoding="utf-8") as f:
    json.dump(positive_case, f, indent=4)

print("✅ All demo files created successfully!")