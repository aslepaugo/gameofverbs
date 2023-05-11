# Support Bot

This bot can answer common user questions. 

The bot works with [Telegram](https://telegram.org/) and [VKontakte](https://vk.com/).

Example output for [Telegram](https://telegram.org/):

![](https://dvmn.org/filer/canonical/1569214094/323/)

Example output for [VKontakte](https://vk.com/):

![](https://dvmn.org/filer/canonical/1569214089/322/)


## How to install

You need to register a bot in [Telegram](https://telegram.org/) and get API key in [VKontakte](https://vk.com/).

Python3 should be already installed. Then use pip (or pip3 if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```

## How to launch

Launch on [Telegram](https://telegram.org/):

```
python tg_bot.py
```

Launch on [VKontakte](https://vk.com/):

```
python vk_bot.py
```

Launch training of the bot:

```
python tg_bot.py --train
``` 

## Environment variables

TG_BOT_API_KEY - Telegram bot API key. You can get it from [BotFather](https://telegram.me/BotFather)

TG_ADMIN_CHAT_ID - Telegram chat ID for sending errors and logs. You can get it from [userinfobot](https://telegram.me/userinfobot)

GCP_API_KEY - Google Cloud Platform API key. You can get it from [Credentials Google Cloud Platform](https://console.cloud.google.com/apis/credentials)

PROJECT_ID - Google Cloud Platform project ID. You can get it from [Google Cloud Platform Common](https://cloud.google.com/)

LANGUAGE_CODE - Language code for DialogFlow. You can get it from [DialogFlow Google Cloud Platform](https://dialogflow.cloud.google.com/#/editAgent/newagent-csrj/languages)

VK_API_KEY - VKontakte API key. You can get it from [VKontakte](https://vk.com/)
