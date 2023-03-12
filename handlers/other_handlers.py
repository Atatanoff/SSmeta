from aiogram.types import Message
from aiogram import Router

router = Router()

@router.message()
async def echo(message: Message):
    await message.answer(message.text)