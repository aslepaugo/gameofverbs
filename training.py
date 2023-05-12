
import json
import logging
import os

from argparse import ArgumentParser
from dialogflow_utils import create_intent
from dotenv import load_dotenv


logger = logging.getLogger(__name__)


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser()
    parser.add_argument("--path", type=str)
    parser.add_argument("--lang", type=str, default=os.environ["LANGUAGE_CODE"])
    args = parser.parse_args()

    with open(args.path, "r", encoding='utf8') as f:
        data = json.load(f)
    for topic, value in data.items():
        intent = create_intent(
            project_id=os.environ["PROJECT_ID"],
            display_name=topic,
            training_phrases_parts=value['questions'],
            message_texts=[value['answer']],
            language_code=args.lang
        )
        logger.info(f"Intent created: {intent}")
