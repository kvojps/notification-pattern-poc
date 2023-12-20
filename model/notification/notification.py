class Notification():
    def __init__(self, message: str, description: str):
        self._message = message
        self._description = description

    def to_dict(self):
        return {"message": self._message, "description": self._description}
