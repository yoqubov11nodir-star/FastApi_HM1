from fastapi import APIRouter, Request

router = APIRouter(prefix='/app_1')

@router.get('/')
async def app_views():
    return {'app': 'website'}

@router.get('/testing/')
async def indexing():
    return {'messge': 'test is done'}

@router.post('/info')
async def data(request: Request):
    data = await request.json()
    return {'title': data.get('title')}

@router.post('/types')
async def types(request: Request):
    data = await request.json()
    return {'type': data.get('type')}