from fastapi import APIRouter

router = APIRouter()

@router.post("/auth/sign_up")
def sign_up():
    print("hi from sign up")
    return "hi from sign up"