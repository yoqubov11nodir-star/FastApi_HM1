from fastapi import FastAPI
from app1.urls import router as app1_router
from app2.urls import router as app2_router

app = FastAPI()
app.include_router(router=app1_router)
app.include_router(router=app2_router)

@app.get('/')
async def test():
    return {'message': 'test'}