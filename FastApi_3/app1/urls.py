from fastapi import APIRouter, Request

router = APIRouter(prefix='app1')

@router.get('/')
async def app1_list():
    return {'app': 'ebook, audio'}

@router.get('/text/')
async def index():
    return {'text': 'text'}

@router.post('/data')
async def data_get(request: Request):
    data = await request.json()
    return {'title': data.get('title')}

@router.post('/info')
async def get_info(request: Request):
    data = await request.json()
    return {'creted_data': data.get('creted_data')}