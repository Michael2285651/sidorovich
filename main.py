from config import TOKEN
from telebot import types
from telebot.async_telebot import AsyncTeleBot
import asyncio
import keyboards

bot = AsyncTeleBot(TOKEN)
storage = {}


@bot.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(
        message.chat.id,
        "Здоров сталкере, як я бачу ти тут новенький, тож давай я тобі розповім, що й до чого. "
        "Для початку я не представився — мене звати Сидорович. Я тутешній торговець і можу "
        "розповісти тобі багато чого цікавого про Чорнобильську зону відчуження. Почнемо?",
        reply_markup=keyboards.questions
    )


@bot.message_handler(commands=["help"])
async def help(message: types.Message):
    await bot.send_message(
        message.chat.id,
        "/start — Start bot\n/help — Help"
    )

@bot.callback_query_handler(func=lambda call: True)
async def callback_qeury(call: types.CallbackQuery):
    try:
        if call.data == "inline_1":
            await bot.answer_callback_query(call.id, text="Ви натиснули inline_1")
            await bot.send_message(call.message.char.id, "Ви натиснули inline_1")
        if call.data == "inline_2":
            await bot.answer_callback_query(call.id, text="Ви натиснули inline_2")
            await bot.send_message(call.message.char.id, "Ви натиснули inline_2")
    except Exception as e:
        print(f"Error: {e}")

@bot.message_handler(content_types=['text'])
async def query(message: types.Message):
    text = message.text.lower()

    if 'привіт' in text:
        await bot.send_message(message.chat.id, 'Здоров')
    elif 'як життя' in text:
        await bot.send_message(message.chat.id, 'Та норм')
    elif 'бувай' in text:
        await bot.send_message(message.chat.id, 'Вдалого полювання сталкере')
    else:
        await bot.send_message(message.chat.id, 'Нічого не зрозумів')


async def main():
    await bot.remove_webhook()
    await bot.infinity_polling(skip_pending=True)


if __name__ == "__main__":
    asyncio.run(main())