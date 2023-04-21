from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state

from keyboards.button import get_start_kb
from services.orm.bd_model import User


router = Router()  # [1]


@router.message(Command(commands=["start"]), StateFilter(default_state))  # [2]
async def cmd_start(message: Message):
    usr = User.get_or_create(id = message.from_user.id)
    print(usr)
    
    await message.answer(
        f"Здраствуйте, {message.from_user.first_name}!",
        reply_markup=get_start_kb()
    )
    await message.delete()
