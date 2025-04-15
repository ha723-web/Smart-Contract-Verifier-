import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_with_llm(code: str) -> str:
    prompt = f"""
You are a smart contract security expert. Review the following Solidity contract for vulnerabilities, gas inefficiencies, and improvements. Provide a summary and actionable suggestions:

{code}
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error contacting LLM: {e}"