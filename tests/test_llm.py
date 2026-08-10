from app.services.llm_service import generate_answer


prompt = """
Responda em português.

Pergunta:
Quais convênios a clínica atende?

Contexto:
A clínica atende:

Unimed
Bradesco Saúde
SulAmérica
Amil

Responda de forma objetiva utilizando apenas as informações do contexto.
"""


answer = generate_answer(prompt)

print("=" * 60)
print("RESPOSTA DO OLLAMA")
print("=" * 60)
print(answer)