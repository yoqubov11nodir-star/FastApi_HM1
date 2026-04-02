from fastapi import APIRouter, Request

router = APIRouter(prefix='/products')

@router.get('/')
async def products_view():
    return {'products': 'Phone, Laptop, Gadget'}

@router.get('/test/')
async def index():
    return {'message': 'test'}

@router.post('/info')
async def data_get(request: Request):
    data = await request.json()
    return {'title': data.get('title'), 'create_date': data.get('create_date')}

@router.post('/type')
async def type_data(request: Request):
    data = await request.json()
    return {'type': data.get('type')}