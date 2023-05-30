import requests
from aiogram import Router, types
from aiogram import F

import config
import json

router = Router()


@router.message(F.text)
async def message_handler(message: types.Message):
    rasa_response = requests.post(
        config.RASA_API_URL,
        json={
            "sender": message.from_user.id,
            "message": message.text
        }
    ).json()

    kb = [[ types.KeyboardButton(text="Неверный ответ") ],]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Неверный ответ"
    )

    answer = '\n'.join([item['text'] for item in rasa_response])

    await message.answer(answer, reply_markup=keyboard)
