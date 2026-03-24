from sentiment_model import analyze_entry

def detect_spiral(history, window=3):
    if len(history) < window:
        return False
    
    last_entries = history[-window:]
    return all(entry["label"] == "NEGATIVE" for entry in last_entries)


def process_entry(text, history):
    # Analyze sentiment
    label, score = analyze_entry(text)

    # Add to history
    history.append({
      "day": len(history) + 1,
      "label": label,
      "score": score
    })

    # Detect spiral
    spiral = detect_spiral(history)

    return {
        "label": label,
        "score": score,
        "history": history,
        "spiral": spiral
    }