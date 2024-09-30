from core.config import app
from baml_handlers.categorize_chat_message_handler import categorize_user_message
from baml_handlers.extract_product_description_from_chat_message import extract_product_description_from_message
from baml_handlers.extract_product_price_from_chat_message import extract_product_price_from_message

from models.request.create_chat_message_request import CreateChatMessageRequest
from models.response.create_chat_message_response import CreateChatMessageResponse
from baml_client.types import MessageCategory
from core.similarity_helper import *
from database.data_helpers import *
from database.in_memory_db import products_embeddings
from core.constants import AssistantMessages

@app.post("/v1/chat/message/")
async def handle_new_chat_message_from_user(new_message : CreateChatMessageRequest):
  message_category = await categorize_user_message(new_message.text)
  response_string = AssistantMessages.ASSISTANT_MESSAGE_SORRY_MESSAGE

  if message_category is MessageCategory.QuestionAboutProductDescription:
    product_description_by_user = await extract_product_description_from_message(new_message.text)
    similarity_df = get_similarity_dataframe(product_description_by_user, products_embeddings, General.GET_TOP_X_RESULTS_FROM_SIMILARITY_DATAFRAME)
    products_with_titles_and_prices = get_products_with_prices_string(similarity_df)
    response_string = AssistantMessages.ASSISTANT_MESSAGE_RECOMMENDED_PRODUCTS.format(products_with_titles_and_prices)

  elif message_category is MessageCategory.QuestionAboutProductPrice:
    product_price_masks = await extract_product_price_from_message(new_message.text)
    products_applied_price_mask = apply_mask_for_dataframe(products_embeddings, product_price_masks)
    products_with_prices_string = get_products_with_prices_string(products_applied_price_mask)
    response_string = AssistantMessages.ASSISTANT_MESSAGE_PRODUCTS_BETWEEN_PRICE.format(products_with_prices_string)

  return CreateChatMessageResponse(text=response_string)