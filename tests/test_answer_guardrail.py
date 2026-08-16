from unittest.mock import patch

from app.services.answer_service import answer_question


FALLBACK_ANSWER = "Não encontrei informações suficientes nos documentos."


print("=" * 70)
print("TESTE DE INTEGRAÇÃO - ANSWER SERVICE + GUARDRAILS")
print("=" * 70)


# ============================================================
# TESTE 1 - Pergunta sem informação suficiente
# ============================================================

print("\n" + "=" * 70)
print("TESTE 1 - Guardrail deve bloquear o LLM")
print("=" * 70)

question = "Qual é o endereço da clínica?"

fake_search_results = [
    {
        "filename": "consultas.md",
        "text": "As consultas devem ser agendadas com antecedência.",
        "similarity": 0.20
    }
]


with patch(
    "app.services.answer_service.search_documents",
    return_value=fake_search_results
), patch(
    "app.services.answer_service.generate_answer"
) as mock_generate_answer:

    result = answer_question(question)

    print(f"Pergunta: {question}")
    print(f"Resposta: {result}")

    if result == FALLBACK_ANSWER and not mock_generate_answer.called:
        print("STATUS: PASSOU")
        print("O LLM não foi chamado.")
    else:
        print("STATUS: FALHOU")
        print("O LLM foi chamado ou o fallback não foi retornado.")


# ============================================================
# TESTE 2 - Pergunta com informação suficiente
# ============================================================

print("\n" + "=" * 70)
print("TESTE 2 - Guardrail deve permitir o LLM")
print("=" * 70)

question = "Quais convênios a clínica atende?"

fake_search_results = [
    {
        "filename": "convenios.md",
        "text": (
            "# Convênios\n\n"
            "A clínica atende:\n\n"
            "Unimed\n"
            "Bradesco Saúde\n"
            "SulAmérica\n"
            "Amil"
        ),
        "similarity": 0.73
    }
]


with patch(
    "app.services.answer_service.search_documents",
    return_value=fake_search_results
), patch(
    "app.services.answer_service.generate_answer",
    return_value="A clínica atende Unimed, Bradesco Saúde, SulAmérica e Amil."
) as mock_generate_answer:

    result = answer_question(question)

    print(f"Pergunta: {question}")
    print(f"Resposta: {result}")

    if mock_generate_answer.called:
        print("STATUS: PASSOU")
        print("O LLM foi chamado após os guardrails permitirem a busca.")
    else:
        print("STATUS: FALHOU")
        print("O LLM não foi chamado.")


print("\n" + "=" * 70)
print("FIM DOS TESTES")
print("=" * 70)