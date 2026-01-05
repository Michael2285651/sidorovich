# 1️⃣ Імпорти
from telegram import Update, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
import config
import keyboards

# 2️⃣ Обробник команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 2.1 Reply-клавіатура під полем введення
    await update.message.reply_text(
        "Привіт! Кнопки під полем введення 👇",
        reply_markup=keyboards.reply_keyboard()  # тут викликаємо функцію з keyboards.py
    )
    
    # 2.2 Inline-клавіатура всередині повідомлення
    inline = InlineKeyboardMarkup([
        [InlineKeyboardButton("Inline 1", callback_data="inline_1"),
         InlineKeyboardButton("Inline 2", callback_data="inline_2")],
        [InlineKeyboardButton("Закрити", callback_data="close")]
    ])
    await update.message.reply_text("А це Inline кнопки 👇", reply_markup=inline)

# 3️⃣ Обробник Reply-кнопок (під полем введення)
async def reply_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Вихід":
        await update.message.reply_text("Закрили клавіатуру.", reply_markup=ReplyKeyboardRemove())
    else:
        await update.message.reply_text(f"Ти натиснув Reply кнопку: {text}")

# 4️⃣ Обробник Inline-кнопок
async def inline_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # обов'язково!!!

    if query.data == "inline_1":
        await query.edit_message_text("Ти натиснув Inline 1!")
    elif query.data == "inline_2":
        await query.edit_message_text("Ти натиснув Inline 2!")
    elif query.data == "close":
        await query.edit_message_text("Inline клавіатура закрита.")

# 5️⃣ Запуск Application
def main():
    app = Application.builder().token(config.TOKEN).build()

    # 5.1 Додаємо /start
    app.add_handler(CommandHandler("start", start))
    
    # 5.2 Додаємо обробник Reply-кнопок
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_handler))
    
    # 5.3 Додаємо обробник Inline-кнопок
    app.add_handler(CallbackQueryHandler(inline_callback))

    print("БОТ ПРАЦЮЄ")
    app.run_polling()

# 6️⃣ Точка входу
if __name__ == "__main__":
    main()
