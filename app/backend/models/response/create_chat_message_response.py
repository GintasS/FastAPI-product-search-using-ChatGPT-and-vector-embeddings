from pydantic import BaseModel

class CreateChatMessageResponse(BaseModel):
    text: str