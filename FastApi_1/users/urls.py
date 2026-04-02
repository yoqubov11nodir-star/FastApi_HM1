from fastapi import APIRouter, Request

router = APIRouter(prefix='/users')

@router.get('/')
async def users_list():
    return {'users': 'ali, vali, dilshod'}

@router.get('/test/')
async def index():
    return {'message': 'test'}

@router.post('/data')
async def data_get(request: Request):
    data = await request.json()
    return {'name': data.get('name'), 'age': data.get('age')}

@router.post('/info')
async def info_get(request: Request):
    data = await request.json()
    return {'level': data.get('level'), 'city': data.get('city')}