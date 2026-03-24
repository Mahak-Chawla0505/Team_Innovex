import streamlit as st
import pandas as pd
from backend.utils import process_entry

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="MoodMentor", layout="centered")

st.title("🧠 MoodMentor")
st.subheader("Your private AI journaling companion")

# -----------------------------
# Session State (ONLY ONCE)
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "last_result" not in st.session_state:
    st.session_state.last_result = None

# -----------------------------
# Sidebar Summary
# -----------------------------
st.sidebar.title("📊 Mood Summary")
st.sidebar.write(f"Total Entries: {len(st.session_state.history)}")

if st.session_state.history:
    df_sidebar = pd.DataFrame(st.session_state.history)
    avg_score = df_sidebar["score"].mean()
    st.sidebar.metric("Average Mood Score", f"{avg_score:.2f}")

# -----------------------------
# Journal Input
# -----------------------------
st.markdown("### ✍️ Write your thoughts")

entry = st.text_area("How are you feeling today?", height=150)

# -----------------------------
# Analyze Button (ONLY LOGIC HERE)
# -----------------------------
if st.button("Analyze Entry"):
    if entry.strip() == "":
        st.warning("Please write something first.")
    else:
        with st.spinner("Analyzing your emotions..."):
            result = process_entry(entry, st.session_state.history)

            # Save state
            st.session_state.history = result["history"]
            st.session_state.last_result = result

# -----------------------------
# Display Last Result (NO REPROCESSING)
# -----------------------------
if st.session_state.last_result:
    result = st.session_state.last_result

    label = result["label"]
    score = result["score"]
    spiral = result["spiral"]

    st.markdown("### 🧠 Your Mood")

    if label == "POSITIVE":
        st.success(f"🙂 Positive ({score:.2f})")
    elif label == "NEGATIVE":
        st.error(f"😞 Negative ({score:.2f})")
    else:
        st.info(f"😐 Neutral ({score:.2f})")

# -----------------------------
# Mood Trend Graph
# -----------------------------
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)

    st.markdown("### 📈 Mood Over Time")
    st.line_chart(df["score"])

    # -----------------------------
    # Sentiment Distribution
    # -----------------------------
    st.markdown("### 📊 Sentiment Distribution")
    st.bar_chart(df["label"].value_counts())

# -----------------------------
# Spiral Alert (CLEAN + ETHICAL)
# -----------------------------
if st.session_state.last_result and st.session_state.last_result["spiral"]:
    st.markdown("### ⚠️ Gentle Check-in")

    st.warning(
        "We've noticed a sustained low mood pattern 💙\n\n"
        "You're not alone — would you like to explore support options?"
    )

    if st.button("View Support Resources"):
        st.info(
            "📌 Campus Counsellor: counsellor@college.edu\n\n"
            "📌 Helpline: 1800-123-456\n\n"
            "📌 Try talking to a friend or taking a short walk 🌿"
        )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("🔐 Your journal is private. Only mood patterns are analyzed.")