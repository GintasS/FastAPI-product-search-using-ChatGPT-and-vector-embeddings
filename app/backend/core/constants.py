import os
from dotenv import load_dotenv

load_dotenv()

class File:
  PRODUCT_EMBEDDINGS_FILE_PATH = "app//backend//static/product_embeddings.csv"
  PRODUCT_INPUT_FILE_PATH = "app//backend//static/product_input.csv"

class General:
  GET_TOP_X_RESULTS_SIMILARITY_DF = 5
  SIMILARITIES_RESULTS_THRESHOLD = 0.80
  SIMILARITIES_RESULTS_MINIMUM_THRESHOLD = 0.5
  

class AssistantMessages:
  ASSISTANT_MESSAGE_PRODUCT_SIMILARITY_SEARCH_FAILURE = "We failed to find similar products from your search."
  ASSISTANT_MESSAGE_INVALID_DESCRIPTION = "We failed to found products that correspond to your description."
  ASSISTANT_MESSAGE_INVALID_PRICE_RANGE = "We failed to get products between the price range."

class OPENAI:
  API_KEY = str(os.environ['OPENAI_API_KEY'])
  EMBEDDING_MODEL = "text-embedding-ada-002"