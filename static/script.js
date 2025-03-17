window.onload = function() {
    function sendMessage() {
        let userInput = document.getElementById("user-input");  // Récupère l'élément input
        let chatBox = document.getElementById("chat-box");

        if (userInput.value.trim() === "") return;

        let userMessage = `<div class="chat-message user">${userInput.value}</div>`;
        chatBox.innerHTML += userMessage;

        fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userInput.value })
        })
        .then(response => response.json())  
        .then(data => {
            let botMessage = `<div class="chat-message bot">${data.response}</div>`;
            chatBox.innerHTML += botMessage;
            chatBox.scrollTop = chatBox.scrollHeight;  
        })
        .catch(error => {
            console.error("Error:", error);  
        });

        userInput.value = "";  
    }

    document.getElementById("send-btn").onclick = sendMessage;
};
