from telegram.ext import CallbackContext
from telegram import Update, ParseMode


greetings =\
    '<b>Привет!</b>\n\n'\
    'Я бот для борьбы со <b>спамом</b>\n'\
    '... todo ...'


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=greetings, parse_mode=ParseMode.HTML)


def msg(update: Update, context: CallbackContext):
    pass
