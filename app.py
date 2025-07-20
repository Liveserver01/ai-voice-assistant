from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return "🤖 Welcome to AI Joke Bot!"

@app.route('/joke')
def get_joke():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Tell me a funny short joke"}]
    )
    joke = response.choices[0].message["content"]
    return jsonify({"joke": joke})

if __name__ == "__main__":
    app.run(debug=True)
