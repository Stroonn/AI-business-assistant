# AI Business Assistant 🤖

Projeto desenvolvido para automatizar tarefas empresariais utilizando Inteligência Artificial.

## 🚀 Tecnologias
- FastAPI
- Python
- Groq API (LLM)
- Uvicorn

## 💡 Funcionalidades
- Chat com IA para análise de dados
- Resumos automáticos
- Estrutura pronta para automações empresariais

## ▶️ Como rodar

<pre><code>pip install -r requirements.txt
uvicorn app.main:app --reload</code></pre>

## 🔐 Variáveis de ambiente

Crie um arquivo .env:

<pre><code>GROQ_API_KEY=sua_chave_aqui</code></pre>

## 📌 Exemplo de uso

Endpoint:
POST /ai/ask

<pre><code>{
  "prompt": "Resuma uma nota fiscal de 1500 reais"
}</code></pre>

## 📄 Upload de PDF

Permite enviar documentos PDF para análise automática com IA.

- Extração de texto
- Identificação de informações relevantes
- Classificação do documento

Endpoint:
POST /pdf/upload