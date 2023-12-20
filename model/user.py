from beanie import Document


class User(Document):
    name: str
    email: str
    cpf: str
    age: int
