import streamlit as st
import pandas as pd
import time
import os

st.title("📊 Real-Time System Performance Dashboard")

log_file = "system_metrics_log.csv"

if not os.path.exists(log_file):
    st.error("Metrics log file not found. Please run 'monitor.py' first.")
    st.stop()

placeholder = st.empty()

start_time = time.time()
duration = 300  # 5 minutes

while time.time() - start_time < duration:
    try:
        df = pd.read_csv(log_file)
        latest = df.tail(1)

        cpu = latest["CPU_Usage(%)"].values[0]
        memory = latest["Memory_Usage(%)"].values[0]
        gpu = latest["GPU_Usage(%)"].values[0]

        with placeholder.container():
            st.metric("CPU Usage (%)", f"{cpu}%")
            st.metric("Memory Usage (%)", f"{memory}%")
            st.metric("GPU Usage (%)", f"{gpu}%" if gpu != 'N/A' else "Not Available")

            st.line_chart(df[["CPU_Usage(%)", "Memory_Usage(%)"]])

        time.sleep(2)

    except Exception as e:
        st.error(f"Error: {e}")
        time.sleep(2)

st.success("✅ 5-minute monitoring session completed.")
