import os
import weaviate
import cohere
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from weaviate.auth import AuthApiKey

load_dotenv()

app = Flask(__name__)

W_URL = os.getenv("WEAVIATE_URL")
W_KEY = os.getenv("WEAVIATE_API_KEY")
C_KEY = os.getenv("COHERE_API_KEY")

co = cohere.Client(C_KEY)


def get_ai_response(question):
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=W_URL,
        auth_credentials=AuthApiKey(W_KEY),
        headers={"X-Cohere-Api-Key": C_KEY}
    )
    try:
        movies_coll = client.collections.get("Movie")
        response = movies_coll.query.near_text(query=question, limit=3)

        context = ""
        for obj in response.objects:
            context += f"Title: {obj.properties.get('title')}, Description: {obj.properties.get('description')}\n"

        # 2. GENERATION
        full_message = f"Use this context to answer in English:\n{context}\n\nQuestion: {question}"
        ai_response = co.chat(message=full_message)
        return ai_response.text
    finally:
        client.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question')
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    answer = get_ai_response(user_question)
    return jsonify({"answer": answer})


if __name__ == '__main__':
    app.run(debug=True)