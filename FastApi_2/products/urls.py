from fastapi import APIRouter, Request

router = APIRouter(prefix='/products')

@router.get('/')
async def product_list():
    return {'products': 'BMW, Audi, Mercedes'}

@router.get('/test/')
async def testing():
    return {'message': 'testing done'}

@router.post('/get_data')
async def get_data(request: Request):
    data = await request.json()
    return {'title': data.get('title'), 'id': data.get('id')}

@router.post('/infos')
async def informations(request: Request):
    data = await request.json()
    return {'created_date': data.get('created_date')}