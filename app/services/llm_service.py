import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:1.7b"

FALLBACK_ANSWER = "Não foi possível gerar uma resposta no momento."

def generate_answer(question, context):
    prompt = f"""
Você é um assistente de uma clínica.

Responda à pergunta SOMENTE usando as informações presentes no CONTEXTO.

Regras:
1. Não invente informações.
2. Não use conhecimento externo.
3. Não faça suposições.
4. Não transforme uma informação em outra que não esteja explicitamente no contexto.
5. Se a resposta não estiver no contexto, diga:
   "Não encontrei informações suficientes nos documentos."
6. Responda em português.
7. Seja objetivo.
8. Não crie procedimentos, prazos, valores, horários ou regras que não estejam escritos no contexto.
9. Responda somente o que a pergunta solicita.
10. Não transforme várias informações do contexto em uma lista de etapas, procedimento ou instruções, a menos que o contexto apresente explicitamente essas etapas.
11. Não combine informações diferentes do contexto para criar uma resposta que não esteja explicitamente apresentada.
12. Se a pergunta pedir uma informação que não estiver explicitamente respondida no contexto, diga:
"Não encontrei informações suficientes nos documentos."
13. Para perguntas do tipo "Como faço para...", só forneça instruções se o contexto explicar explicitamente como realizar aquela ação.

CONTEXTO:
{context}

PERGUNTA:
{question}

RESPOSTA:
"""

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]

    except requests.exceptions.ConnectionError:
        print("[ERRO] Não foi possível conectar ao Ollama.")
        return FALLBACK_ANSWER

    except requests.exceptions.Timeout:
        print("[ERRO] O Ollama demorou muito para responder.")
        return FALLBACK_ANSWER

    except requests.exceptions.RequestException as error:
        print(f"[ERRO] Falha na comunicação com Ollama: {error}")
        return FALLBACK_ANSWER

    except (KeyError, ValueError):
        print("[ERRO] Resposta inválida recebida do Ollama.")
        return FALLBACK_ANSWER