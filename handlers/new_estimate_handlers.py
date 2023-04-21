from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Text, StateFilter
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from datetime import date

from keyboards.button import create_estimates_kb, room_kb
from bot_fsm.fsm_class import FSMWorkEstimate
from services.estimate import rooms
from services.room import Room




router = Router()


storage = RedisStorage('localhost')


@router.callback_query(Text(text='new_estimate'), StateFilter(default_state))
async def new_estimate(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
            text="Введите название сметы...", reply_markup=None)
    await state.set_state(FSMWorkEstimate.create_est)


@router.message(StateFilter(FSMWorkEstimate.create_est))
async def creat_est(message: Message, state: FSMContext):
    
    #est = Estimates(name=message.text, date_create=date)
    await message.answer(text=rooms.name, reply_markup=create_estimates_kb())
    await state.clear()


@router.callback_query(Text(text='add_room'), StateFilter(default_state))
async def creat_room(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Введите название комнаты",
                                      reply_markup=None)
    await state.set_state(FSMWorkEstimate.edit_room)


@router.message(StateFilter(FSMWorkEstimate.edit_room))
async def win_room(message: Message):
    await message.answer(text=message.text,
                            reply_markup=room_kb())


@router.message(StateFilter(FSMWorkEstimate.num_int))
async def count_angle(messge: Message):
    if messge.text.isdigit():
        room = Room(int(messge.text))
        room.name = rooms.room_name
        rooms.add_room(room)
    else:
        await messge.edit_text(text="Пожалуйста введите целое число")


# @router.message(FSMWorkEstimate.create_est)
# async def create_room(message: Message, state: FSMContext):
#     if not rooms.state:
#         rooms.name = message.text
#         await message.answer(text=rooms, reply_markup=cancel_estimates_kb())
#     rooms.state += 1
#     await message.answer(text=rooms, reply_markup=cancel_estimates_kb())

#@router.callback_query() что мы отменяем? Создание сметы или последний ввод?
    
    
    


