import logging

from environs import Env
from telegram import Update
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters

from dialogflow_utils import detect_intent_texts


env = Env()
env.read_env()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2('Здравствуйте. Я бот, который поможет вам.')
    logger.info("Starting start()")


def reply(update: Update, context: CallbackContext):
    try:
        bot_reply = detect_intent_texts(
            env("PROJECT_ID"),
            update.message.from_user.id,
            update.message.text,
            env("LANGUAGE_CODE")
        )
        update.message.reply_text(bot_reply)
    except Exception as e:
        logger.error(e)


def main():
    updater = Updater(env("TG_BOT_API_KEY"))
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    updater.start_polling()


if __name__ == "__main__":
    main()
