import google.generativeai as genai

def configure_gemini(api_key: str):
    genai.configure(api_key=api_key)

def get_ai_insight(stats: dict) -> str:
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")  # Free-tier friendly

    prompt = f"""
    You are a system optimization assistant. Given these system statistics:

    CPU Usage: {stats['cpu']}%
    Memory Usage: {stats['memory']}%
    Disk Usage: {stats['disk']}%
    Network Sent: {stats['net_sent']} MB
    Network Received: {stats['net_recv']} MB

    Provide a simple, human-readable summary of the system performance and suggest any optimizations if needed.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Failed to generate insight: {str(e)}"
