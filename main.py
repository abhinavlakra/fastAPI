from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {
        "message" : "Home Page"
    }

@app.post("/create-user")
def create_user(user:dict):
    return {
        "message": "User Created",
        "data": user
    }
