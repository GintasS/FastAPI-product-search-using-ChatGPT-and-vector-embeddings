from baml_client import b
from baml_client.types import ExtractedProductInformation

import logging

async def extract_product_information_from_message(message : str) -> ExtractedProductInformation:
  try:
    product_information = b.ExtractProductDescriptionAndPriceFromMessage(message)
  except Exception as ex:
    logging.info("[Message Categorizer API] Error on extracting product information from a message.", exc_info=True)
    return None
  return product_information