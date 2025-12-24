DevTwin AI Engine is a web-based intelligent code analysis platform powered by Google Gemini.
It analyzes source code files and provides insights such as architecture understanding, security auditing, and modernization scoring using Google’s Generative AI infrastructure.

🧠 Core Idea

Modern codebases are complex and difficult to evaluate quickly.
DevTwin AI helps developers and evaluators by using Google Gemini AI to:

Understand code structure

Identify security risks

Assess modernization level

Present results in a clean, interactive UI

✨ Features

📂 Upload source files (.java, .py)

🧠 AI-based code analysis using Google Gemini

🏗️ Architecture mapping (visual flow)

🔐 Security audit insights

📊 Modernization score estimation

⚠️ Graceful handling of API quota limits (no crashes)

🎨 Clean, professional Streamlit UI

🛠️ Google Technologies Used
Google Technology	Usage
Google Gemini API	Core AI engine for code analysis
Gemini 1.5 Flash Model	Fast, low-latency generative model
Google GenAI SDK (google.genai)	Official Python SDK for Gemini
Google Cloud / Vertex AI (Express Mode)	API key provisioning & AI infrastructure
Google Cloud Quota System	Demonstrates real production-style limits

🔹 The project is intentionally kept Gemini-only for demo stability.

🧑‍💻 Tech Stack

Frontend & UI: Streamlit (Python)

AI Engine: Google Gemini (GenAI SDK)

Language: Python 3.x

Visualization: Mermaid.js (for architecture flow)

📁 Project Structure
devtwin-gemini/
│
├── app.py          # Main Streamlit application
├── README.md       # Project documentation
└── requirements.txt (optional)

▶️ How to Run the Project
1️⃣ Install Dependencies
pip install streamlit google-genai

2️⃣ Set Google Gemini API Key

Windows (PowerShell):

setx GOOGLE_API_KEY "YOUR_API_KEY_HERE"


Restart terminal after setting.

Verify:

echo $env:GOOGLE_API_KEY

3️⃣ Run the Application
python -m streamlit run app.py


Open in browser:

http://localhost:8501

⚠️ About API Quota Handling

This project uses Google Gemini free-tier API.

If quota is exceeded:

The app does NOT crash

A clear warning message is shown

System remains stable and usable

This behavior reflects real-world production systems, where quota handling is essential.
🚀 Future Scope

Enable billing for unlimited Gemini usage

Add report export (PDF)

Integrate CI/CD pipelines

Deploy on Google Cloud Run

Support more programming languages

👤 Author

DevTwin AI Engine
Built as a demonstration of Google Generative AI integration for intelligent software analysis.
