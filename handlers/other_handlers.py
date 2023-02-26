from aiogram import Dispatcher
from aiogram.types import Message

import pyqrcode

import io
url = pyqrcode.create('http://ya.ru')

def f(url):
    url = pyqrcode.create(url)
    buffer = io.BytesIO()

    url.png(buffer)
    photo = buffer.getvalue()
    return photo



# Этот хэндлер будет реагировать на любые текстовые сообщения пользователя
async def send_echo(message: Message):

    await message.answer_photo(f(message.text))
    


# Функция для регистрации хэндлера
def register_echo_handler(dp: Dispatcher):
    dp.register_message_handler(send_echo)