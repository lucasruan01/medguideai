from flask import Blueprint, request, jsonify
from services.agent_service import ask_agent

chat = Blueprint("chat", __name__)

@chat.route("/chat", methods=["POST"])
def chat_route():
    data = request.get_json()
    question = data["question"]
    answer = ask_agent(question)
    return jsonify({"answer": answer})