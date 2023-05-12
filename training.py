
import json
import logging

from argparse import ArgumentParser
from environs import Env
from dialogflow_utils import create_intent


if __name__ == "__main__":
    env = Env()
    env.read_env()
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    parser = ArgumentParser()
    parser.add_argument("--path", type=str)
    parser.add_argument("--lang", type=str, default=env("LANGUAGE_CODE"))
    args = parser.parse_args()

    with open(args.path, "r", encoding='utf8') as f:
        data = json.load(f)
    for topic, value in data.items():
        intent = create_intent(
            project_id=env("PROJECT_ID"),
            display_name=topic,
            training_phrases_parts=value['questions'],
            message_texts=[value['answer']],
            language_code=args.lang
        )
        logger.info(f"Intent created: {intent}")
