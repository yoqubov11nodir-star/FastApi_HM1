from fastapi import APIRouter, Request

router = APIRouter(prefix='app2')

@router.get('/')
async def app2_list():
    return {'food': 'plov, kebab'}

@router.get('/menu/')
async def menu():
    return {'message': 'Turkish food, Uzbek food'}

@router.post('/menu')
async def menu_get(request: Request):
    data = await request.json()
    return {'menu': data.get('menu')}

@router.post('/informations')
async def information_get(request: Request):
    data = await request.json()
    return {'price': data.get('price')}