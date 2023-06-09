import logging
import os
import random
from time import sleep
import vk_api as vk

from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

from dialogflow_utils import detect_intent_texts
from logger import TelegramBotHandler


logger = logging.getLogger(__name__)


def reply(event, vk_api):
    bot_reply, is_fallback = detect_intent_texts(
        os.environ["PROJECT_ID"],
        event.user_id,
        event.text,
        os.environ["LANGUAGE_CODE"],
        skip_response_on_fallback=True
    )
    if not is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=bot_reply,
            random_id=random.randint(1, 1000)
        )


def main():
    load_dotenv()
    logging.basicConfig(level=logging.INFO)

    vk_session = vk.VkApi(token=os.environ["VK_API_KEY"])
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    tg_bot_api_key = os.environ["TG_BOT_API_KEY"]
    tg_admin_chat_id = os.environ["TG_ADMIN_CHAT_ID"]
    logger_handler = TelegramBotHandler(tg_bot_api_key, tg_admin_chat_id)
    logger_handler.setLevel(logging.WARNING)
    logger_handler.formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    logger.addHandler(logger_handler)

    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    reply(event, vk_api)
        except ConnectionError as e:
            logger.error(e)
            sleep(5)
            continue
        except Exception as e:
            logger.error(e)
            break


if __name__ == "__main__":
    main()
