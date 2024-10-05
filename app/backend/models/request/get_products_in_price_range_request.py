from pydantic import BaseModel

class GetProductsInPriceRangeRequest(BaseModel):
  text: str