from telebot import types

# Список питань для звичайної клавіатури
question_list = ['*Секретка*', 'привіт', 'як життя', 'бувай', 'та просто так']

# ---------------- Reply Keyboard ----------------
questions = types.ReplyKeyboardMarkup(resize_keyboard=True)

for question in question_list:
    questions.add(types.KeyboardButton(question))


# ---------------- Inline Keyboard ----------------
inline_questions = types.InlineKeyboardMarkup(row_width=2)

inline_questions.add(
    types.InlineKeyboardButton(text="Привіт", callback_data="hello"),
    types.InlineKeyboardButton(text="Як життя", callback_data="life"),
    types.InlineKeyboardButton(text="Та просто так", callback_data="just"),
    types.InlineKeyboardButton(text="Бувай", callback_data="bye")
)
