from baml_client import b
from baml_client.types import ProductDescription

import logging

async def extract_product_description_from_message(message : str) -> str:
  try:
    product_description = b.ExtractProductDescriptionFromMessage(message)
  except Exception as ex:
    logging.info("[Message Categorizer API] Error on extracting a product description from a message.", exc_info=True)
    return None
  return product_description