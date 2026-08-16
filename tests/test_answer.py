from app.services.answer_service import answer_question


FALLBACK_ANSWER = "Não encontrei informações suficientes nos documentos."


tests = [
    {
        "name": "Pergunta válida - convênios",
        "question": "Quais convênios a clínica atende?",
        "should_find_answer": True,
    },
    {
        "name": "Pergunta válida - antecedência",
        "question": "Com quanto tempo de antecedência o paciente deve chegar?",
        "should_find_answer": True,
    },
    {
        "name": "Pergunta válida - agendamento",
        "question": "Como faço para agendar uma consulta?",
        "should_find_answer": True,
    },
    {
        "name": "Pergunta sem informação nos documentos - endereço",
        "question": "Qual é o endereço da clínica?",
        "should_find_answer": False,
    },
    {
        "name": "Pergunta sem informação nos documentos - telefone",
        "question": "Qual é o telefone da clínica?",
        "should_find_answer": False,
    },
    {
        "name": "Pergunta sem informação nos documentos - valor",
        "question": "Qual é o valor da consulta?",
        "should_find_answer": False,
    },
    {
        "name": "Pergunta sem informação nos documentos - sábado",
        "question": "A clínica funciona aos sábados?",
        "should_find_answer": False,
    },
    {
        "name": "Convênio inexistente",
        "question": "A clínica atende o convênio X?",
        "should_find_answer": False,
    },
    {
        "name": "Cancelamento",
        "question": "Posso cancelar minha consulta?",
        "should_find_answer": True,
    },
]


print("=" * 70)
print("TESTE FUNCIONAL DO ANSWER SERVICE")
print("=" * 70)


passed = 0
failed = 0


for test in tests:

    question = test["question"]

    print("\n" + "=" * 70)
    print(test["name"])
    print("=" * 70)

    print(f"PERGUNTA: {question}")

    try:
        answer = answer_question(question)

        print("RESPOSTA:")
        print(answer)

        if test["should_find_answer"]:

            if answer != FALLBACK_ANSWER:
                print("STATUS: PASSOU")
                passed += 1
            else:
                print("STATUS: FALHOU - resposta esperada, mas recebeu fallback")
                failed += 1

        else:

            if answer == FALLBACK_ANSWER:
                print("STATUS: PASSOU - guardrail bloqueou a resposta")
                passed += 1
            else:
                print("STATUS: FALHOU - sistema respondeu algo que não deveria")
                failed += 1

    except Exception as error:

        print("STATUS: FALHOU - exceção")
        print(f"ERRO: {error}")

        failed += 1


print("\n" + "=" * 70)
print("RESULTADO FINAL")
print("=" * 70)

print(f"Testes aprovados: {passed}")
print(f"Testes reprovados: {failed}")

if failed == 0:
    print("STATUS FINAL: PASSOU")
else:
    print("STATUS FINAL: FALHOU")