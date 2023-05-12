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

## How to train

```
python training.py --path your_questions.json --lang ru
``` 

Example of the questions:

```
{
    "Устройство на работу": {
        "questions": [
            "Как устроиться к вам на работу?",
            "Как устроиться к вам?",
            "Как работать у вас?",
            "Хочу работать у вас",
            "Возможно-ли устроиться к вам?",
            "Можно-ли мне поработать у вас?",
            "Хочу работать редактором у вас"
        ],
        "answer": "Если вы хотите устроиться к нам, напишите на почту info@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
    },
    "Забыл пароль": {
        "questions": [
            "Не помню пароль",
            "Не могу войти",
            "Проблемы со входом",
            "Забыл пароль",
            "Забыл логин",
            "Восстановить пароль",
            "Как восстановить пароль",
            "Неправильный логин или пароль",
            "Ошибка входа",
            "Не могу войти в аккаунт"
        ],
        "answer": "Если вы не можете войти на сайт, воспользуйтесь кнопкой «Забыли пароль?» под формой входа. Вам на почту придёт письмо с дальнейшими инструкциями. Проверьте папку «Спам», иногда письма попадают в неё."
    }
}
```

 To set up Application Default Credentials, see https://cloud.google.com/docs/authentication/external/set-up-ad

## Environment variables

TG_BOT_API_KEY - Telegram bot API key. You can get it from [BotFather](https://telegram.me/BotFather)

TG_ADMIN_CHAT_ID - Telegram chat ID for sending errors and logs. You can get it from [userinfobot](https://telegram.me/userinfobot)

GCP_API_KEY - Google Cloud Platform API key. You can get it from [Credentials Google Cloud Platform](https://console.cloud.google.com/apis/credentials)

PROJECT_ID - Google Cloud Platform project ID. You can get it from [Google Cloud Platform Common](https://cloud.google.com/)

LANGUAGE_CODE - Language code for DialogFlow. You can get it from [DialogFlow Google Cloud Platform](https://dialogflow.cloud.google.com/#/editAgent/newagent-csrj/languages)

VK_API_KEY - VKontakte API key. You can get it from [VKontakte](https://vk.com/)
