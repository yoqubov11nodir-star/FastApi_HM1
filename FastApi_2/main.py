from fastapi import FastAPI
from products.urls import router as products_router
from workers.urls import router as workers_router

app = FastAPI()
app.include_router(router=products_router)
app.include_router(router=workers_router)

@app.get('/')
async def test():
    return {'message': 'Test'}