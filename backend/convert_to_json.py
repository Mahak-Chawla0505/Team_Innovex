import pandas as pd
import json

# Load CSV
df = pd.read_csv("data/data.csv")

# Define emotion groups
negative_emotions = [
    "afraid", "angry", "anxious", "ashamed",
    "awkward", "bored", "confused", "disgusted",
    "frustrated", "sad", "jealous"
]

positive_emotions = [
    "happy", "excited", "proud", "satisfied",
    "calm", "surprised", "nostalgic"
]

data = []

for _, row in df.iterrows():
    text = row["Answer"]

    neg_score = 0
    pos_score = 0

    # Count emotions
    for emo in negative_emotions:
        if row[f"Answer.f1.{emo}.raw"] == True:
            neg_score += 1

    for emo in positive_emotions:
        if row[f"Answer.f1.{emo}.raw"] == True:
            pos_score += 1

    # Decide label
    if neg_score > pos_score:
        label = "NEGATIVE"
    elif pos_score > neg_score:
        label = "POSITIVE"
    else:
        label = "NEUTRAL"

    data.append({
        "text": text,
        "label": label
    })

# Save JSON
with open("sample_entries.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("✅ JSON file created!")