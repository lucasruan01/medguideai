from app.services.answer_service import answer_question

questions = [
    "Qual é o endereço da clínica?",
    "Qual é o telefone da clínica?",
    "A clínica atende convênio X?",
    "Qual é o valor da consulta?",
    "A clínica funciona aos sábados?",
    "Posso cancelar minha consulta?",
    "Como faço para agendar uma consulta?"
]

for question in questions:
    print("=" * 60)
    print(f"PERGUNTA: {question}")
    print("=" * 60)

    answer = answer_question(question)

    print("RESPOSTA:")
    print(answer)
    print()