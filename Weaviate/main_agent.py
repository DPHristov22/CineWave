import os
import weaviate
import cohere
from dotenv import load_dotenv
from weaviate.auth import AuthApiKey

load_dotenv()

W_URL = os.getenv("WEAVIATE_URL")
W_KEY = os.getenv("WEAVIATE_API_KEY")
C_KEY = os.getenv("COHERE_API_KEY")

co = cohere.Client(C_KEY)
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=W_URL,
    auth_credentials=AuthApiKey(W_KEY),
    headers={"X-Cohere-Api-Key": C_KEY}
)


def ask_ai(question):
    movies_coll = client.collections.get("Movie")
    response = movies_coll.query.near_text(query=question, limit=3)

    context = ""
    for obj in response.objects:
        context += f"Title: {obj.properties.get('title')}, Description: {obj.properties.get('description')}\n"

    full_message = f"User context: {context}\nQuestion: {question}"
    ai_response = co.chat(message=full_message)
    return ai_response.text


print("Movie AI Agent is ready (Secure Mode)!")
print(ask_ai("What movies are in the database?"))
client.close()