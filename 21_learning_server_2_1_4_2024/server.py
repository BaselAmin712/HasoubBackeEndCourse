from fastapi import FastAPI
from routes import auth_router

server = FastAPI()

#routes definitions
server.include_router(auth_router.router)

@server.get("/")
def home():
    print("got req to test")
    return "hi from server"

# endpoint for sign up - creat user with username + password and store them.

# endpoint for sign in - take user given username + password and check them.