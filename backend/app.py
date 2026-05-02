from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    # Simple AI logic (you can improve)
    if "interview" in user_message.lower():
        reply = "Prepare by practicing questions and improving communication."
    elif "sql" in user_message.lower():
        reply = "SQL JOIN combines data from multiple tables."
    else:
        reply = "I'm your AI assistant. Ask me anything!"

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)