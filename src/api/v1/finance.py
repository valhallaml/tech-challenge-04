from fastapi import APIRouter

router = APIRouter()

@router.get('/predict')
async def get_predict():
    return 'Predict'

@router.get('/train')
async def get_train():
    return 'Train'
