from pydantic import BaseModel

class CreateChatMessageRequest(BaseModel):
    text: str