from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8868769905:AAHdQi2XUcYpOcIbicqMgzccjXT8qEAi0Zw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("صلّي على النبي ❤️")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()