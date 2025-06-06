from fastapi import APIRouter

router = APIRouter()

@router.get('/train')
async def get_train():
    return 'Train'
