from openai import OpenAI
from core.constants import *

client = OpenAI(api_key=OPENAI.API_KEY)

def get_embedding(input : str, embedding_model : str):
  http_embedding_response = client.embeddings.create(
    model=embedding_model,
    input=input
  )

  return http_embedding_response.data[0].embedding