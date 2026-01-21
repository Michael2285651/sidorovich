from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types

# 1️⃣ ReplyKeyboard (кнопки під полем введення)
def reply_keyboard():
    return ReplyKeyboardMarkup(
        [
            ["Кнопка 1", "Кнопка 2"],
            ["Вихід"]
        ],
        resize_keyboard=True
    )

# 2️⃣ InlineKeyboard (кнопки всередині повідомлення)
questions = types.InlineKeyboardMarkup(row_width=2)

questions.add(InlineKeyboardButton("Добре давай почнемо", callback_data="Добре давай почнемо")),
questions.add(InlineKeyboardButton("Inline 1", callback_data="Добре давай почнемо")),