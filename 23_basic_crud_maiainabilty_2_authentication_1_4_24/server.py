from fastapi import FastAPI
from routes import students
server = FastAPI()

server.include_router(students.router)

@server.get('/')
def home():
    return {"data": "test"}