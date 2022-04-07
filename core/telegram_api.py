import telebot
import datetime
import logging

from django.conf import settings

# TODO Настроить запуск бота


logger = logging.getLogger(__name__)

telegram_client = telebot.TeleBot(settings.TELEGRAM['TOKEN'])


@telegram_client.message_handler(content_types=['text'])
def get_text_message(message):
    try:
        telegram_client.send_message(message.from_user.id, f'Привет {message.from_user.id}! Ты написал {message.text}')
    except Exception as error:
        logger.error(error)


def run_telegram_bot():
    logger.info(f'Run telegram bot at {datetime.datetime.now()}')
    telegram_client.polling(none_stop=True, interval=0)


def stop_telegram_bot():
    logger.info(f'Stop telegram bot at {datetime.datetime.now()}')
    telegram_client.stop_bot()
