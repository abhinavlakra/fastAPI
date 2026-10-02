from fastapi import FastAPI

app = FastAPI()

# home route.
@app.get('/')
def home():
    return {"message": "welcome to fastapi"}

#about route.
@app.get('/about')
def about():
    return {"mesage": "this is about page"}

# users route,
@app.get('/users')
def users():
    return {
        "users" : ["mohit", "rohit", "amit"]
    }
