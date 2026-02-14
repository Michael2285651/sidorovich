import asyncio
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from config import TOKEN
import keyboards as keyb

bot = AsyncTeleBot(TOKEN)

@bot.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(
        message.chat.id,
        '''Здоров сталкере, як я бачу ти тут новенький, тож давай я тобі розповім, що й до чого. 
        Для початку я не представився — мене звати Сидорович. Я тутешній торговець і можу 
        розповісти тобі багато чого цікавого про Чорнобильську зону відчуження. Почнемо?''',
        reply_markup=keyb.categories
    )

@bot.callback_query_handler(func=lambda call: True)
async def callback_qeury(call: types.CallbackQuery):
    try:
        if call.data == "Добре давай почнемо":
            await bot.send_message(call.message.chat.id, "Отже, що тебе цікавить?", reply_markup=keyb.categories)
        elif call.data == "fractions":
            await bot.send_message(call.message.chat.id, "Ось фракції які є в Зоні", reply_markup=keyb.fractions)
        elif call.data == "anomalyes":
            await bot.send_message(call.message.chat.id, "Ось аномалії які є в Зоні", reply_markup=keyb.anomalyes)
        elif call.data == "weapons":
            await bot.send_message(call.message.chat.id, "Ось зброя яка є в Зоні", reply_markup=keyb.weapons)
        elif call.data == "artifacts":
            await bot.send_message(call.message.chat.id, "Ось артефакти які є в Зоні", reply_markup=keyb.artifacts)
    except Exception as e:
        await bot.send_message(call.message.chat.id, "Шось бошка болить приходь пізніше")


async def main():
    await bot.remove_webhook()
    await bot.infinity_polling(skip_pending=True)


if __name__ == "__main__":
    asyncio.run(main())
    