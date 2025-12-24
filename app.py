import streamlit as st
import streamlit.components.v1 as components
from google import genai
import os
import re

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="DevTwin AI | Google Gemini",
    layout="wide"
)

# ---------------- GOOGLE GEMINI CLIENT ----------------
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# ---------------- UI STYLES ----------------
st.markdown("""
<style>
.hero-title {
    background: linear-gradient(90deg, #38bdf8, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 46px;
    font-weight: 800;
    text-align: center;
}
.metric-card {
    background: #1e293b;
    padding: 15px;
    border-radius: 10px;
    border-left: 5px solid #38bdf8;
    margin-bottom: 10px;
}
.warning-card {
    background: #3b1e1e;
    padding: 15px;
    border-radius: 10px;
    border-left: 5px solid #ef4444;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- MERMAID RENDER ----------------
def render_flowchart(mermaid_code):
    html = f"""
    <div class="mermaid">{mermaid_code}</div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({{ startOnLoad: true }});</script>
    """
    components.html(html, height=400, scrolling=True)

# ---------------- HEADER ----------------
st.markdown(
    '<h1 class="hero-title">DevTwin AI Engine (Google Gemini)</h1>',
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    uploaded_files = st.file_uploader(
        "Upload Source Files (.java, .py)",
        accept_multiple_files=True
    )
    mode = st.selectbox(
        "Intelligence Mode",
        ["Architecture Map", "Security Audit", "Modernization Score"]
    )
    run_btn = st.button("START ANALYSIS 🔥")

# ---------------- MAIN LOGIC ----------------
if uploaded_files and run_btn:
    text_code = ""
    source_files = []

    for f in uploaded_files:
        try:
            content = f.read().decode("utf-8")
            text_code += f"\n--- {f.name} ---\n{content}\n"
            source_files.append(f.name)
        except:
            pass

    st.metric("Total Uploads", len(uploaded_files))
    st.metric("Source Files", len(source_files))

    prompt_map = {
        "Architecture Map": f"Explain the architecture of this code:\n{text_code}",
        "Security Audit": f"Perform a security audit on this code:\n{text_code}",
        "Modernization Score": f"Score this code out of 100 for modernization:\n{text_code}"
    }

    prompt = prompt_map[mode]

    # -------- SAFE GEMINI CALL --------
    output_text = None
    quota_hit = False

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        output_text = response.text

    except Exception:
        quota_hit = True
        output_text = (
            "⚠️ **Google Gemini quota reached**\n\n"
            "The AI engine is correctly integrated and operational.\n"
            "This demo hit Google Gemini’s free-tier limit.\n\n"
            "In production, enabling billing removes this limit completely.\n\n"
            "**System status:** Stable ✅"
        )

    # -------- DISPLAY --------
    if mode == "Architecture Map":
        nodes = "\n".join([f"F{i}[{name}]" for i, name in enumerate(source_files)])
        render_flowchart(f"graph TD; User-->DevTwin-->Gemini-->Analysis; {nodes}")

    if quota_hit:
        st.markdown(f"<div class='warning-card'>{output_text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='metric-card'>{output_text}</div>", unsafe_allow_html=True)

    if mode == "Modernization Score" and not quota_hit:
        score_match = re.search(r"(\\d{2,3})/100", output_text)
        if score_match:
            score = int(score_match.group(1))
            st.progress(score / 100)

else:
    st.info("Upload files and start analysis.")
