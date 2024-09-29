import os
from dotenv import load_dotenv

load_dotenv()

class File:
  PRODUCT_EMBEDDINGS_FILE_PATH = "app//backend//static/product_embeddings.csv"
  PRODUCT_INPUT_FILE_PATH = "app//backend//static/product_input.csv"

class General:
  GET_TOP_X_RESULTS_FROM_SIMILARITY_DATAFRAME = 5

class AssistantMessages:
  ASSISTANT_MESSAGE_RECOMMENDED_PRODUCTS = "Here are some products you might like: {}"
  ASSISTANT_MESSAGE_PRODUCTS_BETWEEN_PRICE = "Here are some products within your price range: {}"
  ASSISTANT_MESSAGE_SORRY_MESSAGE = "I couldn't understand you, do you want to get product recommendations or ask about the price?"

class OPENAI:
  API_KEY = str(os.environ['OPENAI_API_KEY'])
  EMBEDDING_MODEL = "text-embedding-3-small"