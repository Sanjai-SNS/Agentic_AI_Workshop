# agents/persona_agent.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

def identify_persona(startup_description):
    prompt = f"""
    Given the following startup idea, identify the ideal early adopter persona and list relevant online communities where they might be active.
    
    Startup: {startup_description}

    Format:
    Persona: <persona description>
    Communities: <comma-separated list of relevant communities>
    """

    response = llm.invoke(prompt)

    content = response.content.strip()

    if "Communities:" not in content:
        raise ValueError("Response does not contain 'Communities:' section.")

    parts = content.split("Communities:")

    if len(parts) != 2:
        raise ValueError("Response format is invalid. Expected one 'Communities:' section.")

    persona = parts[0].replace("Persona:", "").strip()
    communities = [c.strip() for c in parts[1].split(",") if c.strip()]

    return persona, communities
