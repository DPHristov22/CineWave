import os
import weaviate
import weaviate.classes.config as wvcc
from dotenv import load_dotenv
from weaviate.auth import AuthApiKey

# 1. Load variables from .env
load_dotenv()

W_URL = os.getenv("WEAVIATE_URL")
W_KEY = os.getenv("WEAVIATE_API_KEY")
C_KEY = os.getenv("COHERE_API_KEY")

# 2. Connect to Weaviate
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=W_URL,
    auth_credentials=AuthApiKey(W_KEY),
    headers={"X-Cohere-Api-Key": C_KEY}
)

try:
    print("Connecting to Weaviate...")

    # Delete existing collection if it exists to start fresh
    if client.collections.exists("Movie"):
        client.collections.delete("Movie")
        print("Existing 'Movie' collection deleted.")

    # 3. Create the collection with English Vectorizer
    client.collections.create(
        name="Movie",
        vectorizer_config=wvcc.Configure.Vectorizer.text2vec_cohere(),
        properties=[
            wvcc.Property(name="title", data_type=wvcc.DataType.TEXT),
            wvcc.Property(name="description", data_type=wvcc.DataType.TEXT),
            wvcc.Property(name="year", data_type=wvcc.DataType.INT),
        ]
    )

    # 4. Insert English Data
    movies = client.collections.get("Movie")

    data_rows = [
        {"title": "Inception", "year": 2010,
         "description": "A thief who steals corporate secrets through the use of dream-sharing technology."},
        {"title": "Interstellar", "year": 2014,
         "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."},
        {"title": "The Dark Knight", "year": 2008,
         "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham."}
    ]

    for row in data_rows:
        movies.data.insert(row)
        print(f"Added: {row['title']}")

    print("\nSUCCESS: Database reset and populated with English data!")

finally:
    client.close()
    print("Connection closed.")