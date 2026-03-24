from groq import Groq
import os
from dotenv import load_dotenv
import json

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

def analyze_document(text: str) -> dict:
    prompt = f"""
    Você é um sistema de análise de documentos empresariais.

    Extraia e responda APENAS em JSON válido:

    {{
        "tipo": "",
        "valor": 0,
        "data": "",
        "resumo": ""
    }}

    Regras:
    - Identifique corretamente o tipo (ex: Nota Fiscal, Contrato, Recibo)
    - valor deve ser número
    - data no formato YYYY-MM-DD
    - não escreva nada fora do JSON

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

    content = response.choices[0].message.content

    # limpa markdown
    content = content.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(content)
    except:
        return {"erro": "Falha ao converter resposta", "raw": content}