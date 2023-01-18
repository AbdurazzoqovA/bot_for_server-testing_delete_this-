from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests


def get_activity():
    r = requests.get("http://www.boredapi.com/api/activity/")
    data = r.json()
    return data["activity"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Salom {update.effective_user.first_name}")


async def activity(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(get_activity())


app = (
    ApplicationBuilder().token("5930774111:AAEp_tEadJZdqNqsLZ5CR8_vEXzlpFH_6Ts").build()
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("task", activity))


app.run_polling()
