from aiogram import Router
from aiogram.filters import Text, Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from keyboards.button import get_start_kb
from services import services


router = Router()  # [1]


@router.message(Command(commands=["start"]))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        f"Здраствуйте, {message.from_user.first_name}!",
        reply_markup=get_start_kb()
    )

@router.message(Text("Новая смета"))
async def echo(message: Message):
    pass
    


@router.message(Text("Сметы..."))
async def echo(message: Message):
    await message.answer('Выбираем смету')


@router.message()
async def echo(message: Message):
    await message.answer(message.text)