from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

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
def inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Inline 1", callback_data="inline_1"),
            InlineKeyboardButton("Inline 2", callback_data="inline_2")
        ],
        [
            InlineKeyboardButton("Закрити", callback_data="close")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
