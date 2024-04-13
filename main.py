from fastapi import FastAPI
from Controllers.Controller import CollectionController
import random

app = FastAPI()
controller = CollectionController()
app.include_router(controller.router)

if __name__ == '__main__':
    print("Rodando servidor!")






