from core.config import app
from baml_handlers.extract_product_information_from_message_handler import extract_product_information_from_message
from models.request.create_chat_message_request import CreateChatMessageRequest
from models.response.create_chat_message_response import CreateChatMessageResponse
from models.request.get_products_in_price_range_request import GetProductsInPriceRangeRequest
from core.similarity_helper import *
from database.data_helpers import is_product_description_valid, is_price_range_valid, apply_mask_for_df, get_products_summary
from database.in_memory_db import products_embeddings
from core.constants import AssistantMessages
from core.constants import *

@app.post("/v1/chat/message/")
async def handle_new_chat_message_from_user(request: CreateChatMessageRequest):
  extracted_chat_gpt_request = await extract_product_information_from_message(request.text)
  product_description = extracted_chat_gpt_request.description
  product_price_range = extracted_chat_gpt_request.price_range
  global products
  products = products_embeddings
  filter_was_active = False
  
  if is_product_description_valid(product_description):
    products = get_similarity_df(product_description, products, request.similarities_results_max_count, request.similarities_results_threshold, OPENAI.EMBEDDING_MODEL) 
    filter_was_active = True

  if is_price_range_valid(product_price_range):
    products = apply_mask_for_df(products, product_price_range)
    filter_was_active = True
   
  if len(products) == 0 or filter_was_active is False:
    return CreateChatMessageResponse(text=AssistantMessages.ASSISTANT_MESSAGE_PRODUCT_SIMILARITY_SEARCH_FAILURE)
  
  product_summary = get_products_summary(products)
  return CreateChatMessageResponse(text=product_summary)

@app.post("/v1/chat/product/description/")
async def handle_product_description_request(request: CreateChatMessageRequest):
  extracted_chat_gpt_request = await extract_product_information_from_message(request.text)
  product_description = extracted_chat_gpt_request.description

  if is_product_description_valid(product_description) is False:
    return CreateChatMessageResponse(text=AssistantMessages.ASSISTANT_MESSAGE_INVALID_DESCRIPTION)

  products = get_similarity_df(product_description, products_embeddings, request.similarities_results_max_count, request.similarities_results_threshold, OPENAI.EMBEDDING_MODEL)
  if len(products) == 0:
    return CreateChatMessageResponse(text=AssistantMessages.ASSISTANT_MESSAGE_PRODUCT_SIMILARITY_SEARCH_FAILURE)

  product_summary = get_products_summary(products)
  return CreateChatMessageResponse(text=product_summary)

@app.post("/v1/chat/product/price/")
async def handle_product_price_range_request(request: GetProductsInPriceRangeRequest):
  extracted_chat_gpt_request = await extract_product_information_from_message(request.text)
  product_price_range = extracted_chat_gpt_request.price_range

  if is_price_range_valid(product_price_range) is False:
    return CreateChatMessageResponse(text=AssistantMessages.ASSISTANT_MESSAGE_INVALID_PRICE_RANGE)

  products = apply_mask_for_df(products_embeddings, product_price_range)
  if len(products) == 0:
    return CreateChatMessageResponse(text=AssistantMessages.ASSISTANT_MESSAGE_INVALID_PRICE_RANGE)

  product_summary = get_products_summary(products)
  return CreateChatMessageResponse(text=product_summary)