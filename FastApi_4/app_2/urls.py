from fastapi import APIRouter, Request

router = APIRouter(prefix='/app2')

@router.get('/')
async def app2_lsit():
    return {'Game_type': 'war, football, firghting'}

@router.get('/list')
async def list_game():
    return {'message': 'Call of duty, FC26'}

@router.post('/menu')
async def menu_get(request: Request):
    data = await request.json()
    return {'menu': data.get('menu')}

@router.post('/info')
async def info_get(request: Request):
    data = await request.json()
    return {'price': data.get('price')}