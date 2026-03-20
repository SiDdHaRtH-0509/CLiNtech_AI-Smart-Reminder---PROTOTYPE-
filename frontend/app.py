import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="CLiNtech", layout="wide")

# --- CSS ---
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- HEADER ---
col1, col2 = st.columns([1, 8])

import os
from PIL import Image

with col1:
    base_dir = os.path.dirname(__file__)
    logo_path = os.path.join(base_dir, "assets", "CLiNtech_logo.png")
    logo = Image.open(logo_path)
    st.image(logo, width=50)
    

with col2:
    st.markdown("""
    <div class="title">CLiNtech</div>
    <div class="tagline">Innovate • Adapt • Succeed</div>
    """, unsafe_allow_html=True)

st.write("") 

# --- INPUT ---
col1, col2 = st.columns([3,1])

with col1:
    user_input = st.text_input("🧠 Enter reminder")

with col2:
    if st.button("🎤 Voice"):
        user_input = "Voice feature handled locally"

# --- PROCESS ---
if st.button("⚙️ Process"):
    if user_input:
        parsed = requests.post(f"{API_URL}/parse", json={"text": user_input}).json()

        requests.post(f"{API_URL}/add_reminder", json=parsed)

        st.success("✅ Reminder Added")

        st.subheader("🧠 AI Understanding")
        st.json(parsed)

# --- TRIGGERS ---
st.subheader("⏰ Triggered Reminders")
triggers = requests.get(f"{API_URL}/check_reminders").json()

for t in triggers:
    st.warning(f"🔔 {t['task']}")

# --- SUGGESTIONS ---
st.subheader("💡 Smart Suggestions")
suggestions = requests.get(f"{API_URL}/suggestions").json()

for s in suggestions:
    st.write(s)

# --- SYSTEM FLOW ---
st.subheader("⚙️ System Pipeline")
st.write("Frontend → API → AI → DB → Engine → Response")