from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {
        "message" : "Home Page"
    }

# dynamic user route.
@app.get('/users/{user_id}')
def get_user(user_id:int):
    return {
        "user_id": user_id
    }

# query params. (/users?name="mohit") - used for filtering, searching, sorting.
@app.get('/products')
def get_products(name: str = None, price : int = 0):
    return {
        "Name": name,
        "Price": price
    }

