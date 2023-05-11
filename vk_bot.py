import logging
import random
from time import sleep
import vk_api as vk

from environs import Env
from vk_api.longpoll import VkLongPoll, VkEventType

from dialogflow_utils import detect_intent_texts
from logger import TelegramBotHandler


env = Env()
env.read_env()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def reply(event, vk_api):
    try:
        bot_reply = detect_intent_texts(
            env("PROJECT_ID"),
            event.user_id,
            event.text,
            env("LANGUAGE_CODE"),
            skip_response_on_fallback=True
        )
        if bot_reply:
            vk_api.messages.send(
                user_id=event.user_id,
                message=bot_reply,
                random_id=random.randint(1, 1000)
            )
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    vk_session = vk.VkApi(token=env("VK_API_KEY"))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    tg_bot_api_key = env("TG_BOT_API_KEY")
    tg_admin_chat_id = env("TG_ADMIN_CHAT_ID")
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
