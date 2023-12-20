from pydantic import BaseModel


class Notification(BaseModel):
    message: str
    description: str

    def __init__(self):
        super().__init__()
