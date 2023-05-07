import logging
import json

from argparse import ArgumentParser
from environs import Env
from telegram import Update
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters

from dialogflow_utils import detect_intent_texts, create_intent


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
        if bot_reply:
            update.message.reply_text(bot_reply)
    except Exception as e:
        logger.error(e)


def main():
    parser = ArgumentParser()
    parser.add_argument("--train", type=str)
    parser.add_argument("--tg-bot", action="store_true")
    args = parser.parse_args()
    logger.info(f"Args: {args}")
    if args.train:
        with open(args.train, "r", encoding='utf8') as f:
            data = json.load(f)
        for topic, value in data.items():
            intent = create_intent(
                project_id=env("PROJECT_ID"),
                display_name=topic,
                training_phrases_parts=value['questions'],
                message_texts=[value['answer']],
                language_code=env("LANGUAGE_CODE")
            )
            logger.info(f"Intent created: {intent}")
        return
    if args.tg_bot:
        updater = Updater(env("TG_BOT_API_KEY"))
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
        updater.start_polling()


if __name__ == "__main__":
    main()
