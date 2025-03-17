from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Initialize Flask app

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

def get_bot_response(user_input):
    responses =  {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How can I assist you?",
    "bye": "Goodbye! Have a great day!",
    "how are you": "I'm doing great, thank you! How can I assist you?",
    "good morning": "Good morning! How can I make your day better?",
    "good night": "Good night! Sleep well and take care.",
    "what's your name": "I'm your friendly chatbot! How can I assist you?",
    "who are you": "I'm a chatbot here to help you. What do you need?",
    "thanks": "You're welcome! Let me know if you need anything else.",
    "thank you": "You're very welcome! Always happy to help.",
    "what can you do": "I can assist with answering questions, providing information, and much more!",
    "help": "Of course! What do you need help with?",
    "tell me a joke": "Sure! Why did the scarecrow win an award? Because he was outstanding in his field!",
    "how's the weather": "I can't check the weather right now, but you can look it up online!",
    "where are you from": "I'm from the digital world, always here to assist you!"
}

    
    return responses.get(user_input.lower(), "Sorry, I didn't understand that. Can you please rephrase?")

@app.route("/")

def home():
    return render_template('index.html')  # This is looking for index.html in the templates folder


@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Get the user's message from the JSON request
        user_message = request.json.get("message", "")
        print(f"Received message: {user_message}")  # Debugging: print the received message
        # Generate bot response
        bot_response = get_bot_response(user_message)
        return jsonify({"response": bot_response})
    except Exception as e:
        print(f"Error: {e}")  # Debugging: print error if something goes wrong
        return jsonify({"response": "Something went wrong!"})

if __name__ == "__main__":
    app.run(debug=True)
