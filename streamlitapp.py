# app.py  ── Streamlit version of your Flask crop-recommender
import pickle
import numpy as np
import streamlit as st

# ────────────────────────────────────────────────────────────
# 1) Page config & header
# ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🌾 Crop Recommendation Demo",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("🌱 Crop Recommendation System")
st.write(
    "Enter your soil & climate parameters below and let the model suggest the most suitable crop."
)

# ────────────────────────────────────────────────────────────
# 2) Load your trained model
# ────────────────────────────────────────────────────────────
@st.cache_resource  # keeps the model in memory between reruns
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ────────────────────────────────────────────────────────────
# 3) Collect user inputs
#    Adjust the fields & ranges to match your dataset!
# ────────────────────────────────────────────────────────────
with st.form(key="user_inputs"):
    col1, col2, col3 = st.columns(3)

    N = col1.number_input("Nitrogen (N)", 0.0, 140.0, 50.0, step=1.0)
    P = col2.number_input("Phosphorus (P)", 0.0, 145.0, 50.0, step=1.0)
    K = col3.number_input("Potassium (K)", 0.0, 205.0, 50.0, step=1.0)

    temperature = col1.slider("Temperature (°C)", 0.0, 50.0, 25.0)
    humidity    = col2.slider("Humidity (%)",    10.0, 100.0, 60.0)
    ph          = col3.slider("pH",               3.5,   9.5,  6.5)
    rainfall    = st.slider("Rainfall (mm)",      0.0, 300.0, 90.0)

    submitted = st.form_submit_button("🌾 Predict Best Crop")

# ────────────────────────────────────────────────────────────
# 4) Make prediction & show result
# ────────────────────────────────────────────────────────────
if submitted:
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(features)[0]

    st.success(f"✅ Recommended Crop: **{prediction}**")

    # Optional: show raw probabilities if you have them
    # probs = model.predict_proba(features)[0]
    # st.write("Model confidence:", {cls: f"{p:.1%}" for cls, p in zip(model.classes_, probs)})

# ────────────────────────────────────────────────────────────
# 5) Footer / about section
# ────────────────────────────────────────────────────────────
st.markdown(
    """
---
Built with **[Streamlit](https://streamlit.io)** · Model developed by *Kodamasimham Chaitanya Pranav Sai*  
[GitHub Repo](https://github.com/your-username/your-repo) • [Portfolio](https://pranav.lovable.so)
"""
)
