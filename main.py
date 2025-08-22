from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# === Put your bot token here ===
TOKEN = "YOUR_BOT_TOKEN"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! ✅ Your bot is working.")

# main function
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
