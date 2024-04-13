from fastapi import APIRouter, Form
from ConfigDatabase.Database import MySQLDatabase
from Service.Impl.UserServiceImpl import UserServiceImpl

from .Routes import router as document_router, router
from typing import Annotated
from Model.User import User

db = MySQLDatabase()
user_service = UserServiceImpl()


class CollectionController:
    def __init__(self):
        self.router = APIRouter()
        self.router.include_router(document_router)

    @router.post('/create-user')
    async def create_new_user(user: Annotated[User, Form]):
        create_success = user_service.create_user(user.username, user.email, user.first_name, user.last_name,
                                                  user.password_user)

        if create_success:
            return {"message": "Usuário foi criado com sucesso"}
        else:
            return {"message": "Falha ao criar usuário"}
