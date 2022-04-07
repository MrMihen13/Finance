# Do not remove these 2 lines:
from django.conf import settings


if settings.TELEGRAM['TOKEN']:
    BOT_TOKEN = settings.TELEGRAM['TOKEN']
    APP_NAME = settings.TELEGRAM['BOT_USERNAME']
else:
    raise Exception('Telegram bot token not set in environ')
