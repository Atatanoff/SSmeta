from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text


router = Router()


@router.callback_query(Text(text='new_estimate'))
async def new_estimate(message: Message):
    print(message)    
