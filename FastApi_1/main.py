from fastapi import FastAPI
from products.urls import router as product_router
from users.urls import router as user_router

app = FastAPI()
app.include_router(router=product_router)
app.include_router(router=user_router)

@app.get('/')
async def index():
    return {'message': 'Home page'}