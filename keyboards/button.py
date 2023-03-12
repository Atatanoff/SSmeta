from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def get_start_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="Сметы...", callback_data="estimates")
    kb.button(text="Новая смета", callback_data="new_estimate")
    kb.adjust(2)
    return kb.as_markup()


def create_estimates_kb(lst_buttons=[]):
    kb = InlineKeyboardBuilder()
    kb.button(text="Добавить комнату...", callback_data="add_room")
    for but in lst_buttons:
        kb.button(but, callback_data="")
    return kb.as_markup()


def room_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="Произвести замер...", callback_data="add_size")
    kb.button(text="Добавить проёмы...", callback_data="add_opening")
    kb.button(text="Сохранить комнату в смету", callback_data="save_room")
    kb.button(text="Отмена добавления комнаты", callback_data="cansel_add")
    kb.adjust(1)
    return kb.as_markup()

def cancel_estimates_kb():
    kb = ReplyKeyboardBuilder()
    kb.add(KeyboardButton("Отмена"))
    kb.add(KeyboardButton("Отмена последнего"))
    kb.adjust(2)
    return kb.as_markup()


