# backend/rag/analyzer.py

from vertexai.language_models import ChatModel, InputOutputTextPair
from vertexai.preview.generative_models import GenerativeModel
from typing import List
import os
import vertexai
from vertexai.generative_models import GenerativeModel

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/class/HerculesSec_2.0/keys/gemini-access.json"

vertexai.init(
    project="beaming-bliss-336315",   # 🛠️ Replace this
    location="us-central1"
)

model = GenerativeModel("gemini-2.5-pro")  # or whatever your model is

# Use your preferred Gemini model
MODEL_NAME = "gemini-2.5-pro"


def analyze_vulnerabilities(docs: List[str], user_code: str = "") -> str:
    """Analyze retrieved documentation and source code for vulnerabilities."""

    # Initialize Gemini
    model = GenerativeModel(MODEL_NAME)

    # Combine docs into a context string
    context = "\n\n".join(docs)

    # Prompt for LLM
    prompt = f"""
You are a cybersecurity expert. Analyze the following context and source code for OWASP Top 10 vulnerabilities. 
If any security flaws exist, mention their category (e.g., XSS, Injection), severity (Low, Medium, High), and suggest improvements.

--- Context from documentation ---
{context}

--- User code if any ---
{user_code}

Return the answer in this JSON format:
[
  {{
    "vulnerability": "<name>",
    "description": "<what it is>",
    "severity": "<Low|Medium|High>",
    "recommendation": "<how to fix>"
  }},
  ...
]
"""

    # Call Gemini to generate analysis
    response = model.generate_content(prompt)
    return response.text
