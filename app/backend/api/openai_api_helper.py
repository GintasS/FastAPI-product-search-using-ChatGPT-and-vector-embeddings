from openai import OpenAI
from core.constants import *

client = OpenAI(api_key=OPENAI.API_KEY)

def get_embedding(input : str):
  http_embedding_response = client.embeddings.create(
    model=OPENAI.EMBEDDING_MODEL,
    input=input
  )

  return http_embedding_response.data[0].embedding