import streamlit as st
import psutil
import time
from gemini_utils import configure_gemini, get_ai_insight

# Set page config
st.set_page_config(page_title="AI System Profiler", layout="centered")

st.title("🧠 AI-Enhanced System Performance Profiler")
st.write("Real-time system stats + Gemini-powered insights")

# Input Gemini API Key
api_key = st.text_input("Enter your Gemini API Key", type="password")
if api_key:
    configure_gemini(api_key)

# Get real-time stats
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
net_io = psutil.net_io_counters()
net_sent = round(net_io.bytes_sent / (1024 * 1024), 2)
net_recv = round(net_io.bytes_recv / (1024 * 1024), 2)

st.metric("🖥️ CPU Usage", f"{cpu}%")
st.metric("💾 Memory Usage", f"{memory}%")
st.metric("🗄️ Disk Usage", f"{disk}%")
st.metric("📤 Network Sent", f"{net_sent} MB")
st.metric("📥 Network Received", f"{net_recv} MB")

# Store stats
stats = {
    "cpu": cpu,
    "memory": memory,
    "disk": disk,
    "net_sent": net_sent,
    "net_recv": net_recv
}

# AI Insight
if st.button("🧠 Generate AI Insight"):
    if not api_key:
        st.warning("Please enter your Gemini API key.")
    else:
        with st.spinner("Thinking..."):
            insight = get_ai_insight(stats)
            st.success("AI Suggestion:")
            st.write(insight)
