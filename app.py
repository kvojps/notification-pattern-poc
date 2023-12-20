from fastapi import FastAPI, status, HTTPException

from config.db import init_mongo_db

from user_request import UserRequest

from model.dto.user_dto import UserDTO

from model.user import User

app = FastAPI(
    title="API - Notification pattern POC",
    version="0.1.0",
    description="API Rest validar conceitos do Notification pattern com FastAPI"
)


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=User, tags=["users"])
async def create_user(user_request: UserRequest):
    user_dto = UserDTO(
        name=user_request.name,
        email=user_request.email,
        cpf=user_request.cpf,
        age=user_request.age
    )

    if user_dto.get_notification_context().has_errors():
        raise HTTPException(
            status_code=400, detail=user_dto.get_notification_context().get_errors())

    user = User(
        name=user_dto.get_name(),
        email=user_dto.get_email(),
        cpf=user_dto.get_cpf(),
        age=user_dto.get_age()
    )

    return await user.save()


@app.on_event("startup")
async def start_mongo_db():
    await init_mongo_db()
