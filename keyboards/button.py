from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_start_kb() -> ReplyKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Сметы...", callback_data="estimates")
    kb.button(text="Новая смета", callback_data="new_estimate")
    kb.adjust(2)
    return kb.as_markup()


def get_estimates_kb() -> ReplyKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Добавить комнату", callback_data="estimates")
    kb.button(text="Новая смета", callback_data="new_estimate")
    kb.adjust(2)
    return kb.as_markup()
