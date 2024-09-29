from baml_client import b
from baml_client.types import ProductDescription

import logging

async def extract_product_price_from_message(message : str) -> str:
  try:
    product_price_masks = b.ExtractProductPriceFromMessage(message)
  except Exception as ex:
    logging.info("[Message Categorizer API] Error on extracting a product price from a message.", exc_info=True)
    return None
  return product_price_masks