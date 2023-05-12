import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters

from dialogflow_utils import detect_intent_texts
from logger import TelegramBotHandler


logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2('Здравствуйте. Я бот, который поможет вам.')
    logger.info("Starting start()")


def error_handler(update: Update, error: Exception):
    logger.warning('Update "%s" caused error "%s"', update, error)


def reply(update: Update, context: CallbackContext):
    try:
        bot_reply, _ = detect_intent_texts(
            os.environ["PROJECT_ID"],
            update.message.from_user.id,
            update.message.text,
            os.environ["LANGUAGE_CODE"]
        )
        update.message.reply_text(bot_reply)
    except Exception as e:
        logger.error(e)


def main():
    load_dotenv()
    logging.basicConfig(level=logging.INFO)

    tg_bot_api_key = os.environ["TG_BOT_API_KEY"]
    tg_admin_chat_id = os.environ["TG_ADMIN_CHAT_ID"]
    logger_handler = TelegramBotHandler(tg_bot_api_key, tg_admin_chat_id)
    logger_handler.setLevel(logging.WARNING)
    logger_handler.formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    logger.addHandler(logger_handler)
    updater = Updater(tg_bot_api_key)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    dispatcher.add_error_handler(error_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
