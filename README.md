

# NeoBot - AI Chatbot
![neobot](https://github.com/user-attachments/assets/278c892a-ad21-4ce4-ba9e-c0bc713e9976)


NeoBot is a simple chatbot built using **Flask, Flask-CORS, JavaScript, JSON, HTML, and CSS**. It allows users to interact with a chatbot in real-time, with responses dynamically displayed on the interface.

## Features
✅ **Flask-based API** for handling chat messages.
✅ **JavaScript-powered frontend** for real-time chat updates.
✅ **Cross-Origin compatibility** enabled via Flask-CORS.
✅ **JSON-based communication** for efficient data exchange.
✅ **Responsive UI** built with HTML & CSS.

---

## Technologies Used

### Backend (Python & Flask)
- **Flask** - Lightweight web framework for handling HTTP requests.
- **Flask-CORS** - Enables Cross-Origin Resource Sharing (CORS) for frontend-backend communication.
- **jsonify** - Converts Python dictionaries/lists into JSON responses.

### Frontend (JavaScript, HTML, CSS)
- **JavaScript (Fetch API)** - Sends and receives chat messages dynamically.
- **HTML** - Provides the chatbot’s structure.
- **CSS** - Styles the chatbot UI.

### Data Format
- **JSON** - Used for sending and receiving structured data between frontend and backend.

---

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YASINet12/neobot.git
cd neobot
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3** installed. Then, install Flask and Flask-CORS:
```bash
pip install flask flask-cors
```

### 3️⃣ Run the Backend (Flask Server)
```bash
python app.py
```
The server will start on `http://127.0.0.1:5000/`

### 4️⃣ Open the Frontend
Open `index.html` in your web browser.

---

## Usage
1. Enter a message in the input field.
2. Click the **Send** button.
3. The chatbot will respond dynamically.

---

## API Endpoint
### `POST /chat`
- **Request:**
  ```json
  { "message": "Hello" }
  ```
- **Response:**
  ```json
  { "response": "Hi there! How can I assist you?" }
  ```

---

## Future Improvements
🚀 Add AI-powered responses using NLP
🚀 Improve UI with animations and themes
🚀 Integrate with a database to store chat history

---

## License
This project is licensed under the MIT License.

---

### 😊 Happy Chatting with NeoBot! 😁

