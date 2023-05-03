import logging

from environs import Env
from telegram import Update
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters


env = Env()
env.read_env()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2('Здравствуйте!')
    logger.info("Starting start()")


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)
    logger.info("Starting echo()")


def main():
    updater = Updater(env("TG_BOT_API_KEY"))
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()


if __name__ == "__main__":
    main()
