from flask import Blueprint, request, jsonify
from app.services.answer_service import answer_question

chat = Blueprint("chat", __name__)

@chat.route("/chat", methods=["POST"])
def chat_route():
    try:
        print("Recebi uma pergunta!")

        data = request.get_json()

        if not data:
            return jsonify({
                "answer": "Não foi possível processar a solicitação."
            }), 400

        question = data.get("question")

        if not question or not question.strip():
            return jsonify({
                "answer": "Por favor, informe uma pergunta."
            }), 400

        answer = answer_question(question)

        return jsonify({
            "answer": answer
        })

    except Exception as error:
        print(f"[ERRO] Falha ao processar pergunta: {error}")

        return jsonify({
            "answer": "Ocorreu um erro ao processar sua pergunta."
        }), 500