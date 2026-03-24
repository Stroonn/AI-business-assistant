from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Você é um assistente de negócios inteligente."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def analyze_document(text: str) -> str:
    prompt = f"""
    Você é um sistema de análise de documentos empresariais.

    Extraia e organize as seguintes informações:

    - Tipo de documento
    - Valor total (apenas número)
    - Data
    - Partes envolvidas (se houver)
    - Resumo curto

    Responda de forma clara e organizada.

    Documento:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Especialista em análise de documentos empresariais."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content