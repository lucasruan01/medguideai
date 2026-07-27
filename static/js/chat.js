async function sendQuestion(){

    const question = document.getElementById("question").value;

    const response = await fetch("/chat", {

        method: "POST",

        headers:{
            "Content-Type":"application/json"
        },

        body: JSON.stringify({
            question: question
        })

    });

    const data = await response.json();

    console.log(data.answer);

}