from pydantic import BaseModel


class UserRequest(BaseModel):
    name: str
    email: str
    cpf: str
    age: int
