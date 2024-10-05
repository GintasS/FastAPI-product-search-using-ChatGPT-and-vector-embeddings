from pydantic import BaseModel, Field

class CreateChatMessageRequest(BaseModel):
  text: str
  similarities_results_max_count : int  = Field(default=5)
  similarities_results_threshold : float = Field(gr=0.5, default=0.8)