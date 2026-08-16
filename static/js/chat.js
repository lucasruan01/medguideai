async function sendQuestion() {

    const questionElement = document.getElementById("question");
    const answerElement = document.getElementById("answer");

    const question = questionElement.value.trim();

    if (!question) {
        answerElement.textContent = "Por favor, digite uma pergunta.";
        return;
    }

    answerElement.textContent = "Consultando...";

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        const data = await response.json();

        if (!response.ok) {

            answerElement.textContent =
                data.answer || "Ocorreu um erro ao processar sua pergunta.";

            return;
        }

        answerElement.textContent = data.answer;

    } catch (error) {

        console.error("Erro:", error);

        answerElement.textContent =
            "Não foi possível conectar ao MedGuide AI.";
    }
}