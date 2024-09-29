from baml_client import b
from baml_client.types import MessageCategory

import logging

async def categorize_user_message(message : str) -> MessageCategory:
  try:
    category = b.ExtractMessageCategoryFromMessage(message)
  except Exception as ex:
    logging.info("[Message Categorizer API] Error on categorizing a harmful message.", exc_info=True)
    return MessageCategory.Other
  return category