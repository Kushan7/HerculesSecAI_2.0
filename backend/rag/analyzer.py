from vertexai.preview.generative_models import GenerativeModel
import os
import vertexai
from typing import List
from dotenv import load_dotenv

load_dotenv()

credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if credentials_path:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
else:
    raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS not found in environment or .env file.")

vertexai.init(
    project="beaming-bliss-336315",   # ✅ Replace if needed
    location="us-central1"
)

MODEL_NAME = "gemini-1.5-pro"  # ✅ Adjust if you're not using 2.5 in preview
model = GenerativeModel(MODEL_NAME)

# 👇 Updated to async
async def analyze_vulnerabilities(user_question: str, docs: List[str] = [], user_code: str = "") -> str:
    """
    Analyze source code and/or documentation using Gemini to find OWASP vulnerabilities.
    """

    context = "\n\n".join(docs) if docs else "No docs provided"

    prompt = f"""
You are an Offensive Security Certified Cybersecurity Expert. Analyze the following source code and documentation for OWASP Top 10 vulnerabilities. 
For any issues, provide:
- vulnerability name (e.g., XSS, SQL Injection)
- severity (Low, Medium, High)
- description
- fix recommendation

Format the output in JSON like this:

[
  {{
    "vulnerability": "<name>",
    "description": "<what it is>",
    "severity": "<Low|Medium|High>",
    "recommendation": "<how to fix>"
  }},
  ...
]

--- Context from documentation ---
{context}

--- User code (if any) ---
{user_code}

--- User question ---
{user_question}
"""

    # 👇 Async Gemini call
    try:
        response = await model.generate_content_async([prompt])
        return response.text.strip()
    except Exception as e:
        print(f"[Gemini Error] {e}")
        return "Error analyzing vulnerabilities. Try again later."
