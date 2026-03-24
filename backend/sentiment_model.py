# sentiment_model.py

from transformers import pipeline

# Load model once
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_entry(text):
    """
    Takes journal text and returns:
    label: POSITIVE / NEGATIVE
    score: confidence
    """

    # Safety: handle empty input
    if not text.strip():
        return "NEUTRAL", 0.5

    result = sentiment_analyzer(text[:512])[0]

    label = result["label"]   # POSITIVE / NEGATIVE
    score = result["score"]

    return label, score