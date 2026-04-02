from fastapi import APIRouter, Request

router = APIRouter(prefix='/workers')

@router.get('/')
async def worker_list():
    return {'workers': 'Dilshod, Anvar, Azamat'}

@router.get('/test/')
async def test():
    return {'message': 'test'}

@router.post('/data')
async def data_get(request: Request):
    data = await request.json()
    return {'name': data.get('name'), 'phone': data.get('phone')}

@router.post('/info')
async def info_get(request: Request):
    data = await request.json()
    return {'city': data.get('city'), 'age': data.get('age')}