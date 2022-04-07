import logging

from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.inlinekeyboardbutton import InlineKeyboardButton
from django_tgbot.types.inlinekeyboardmarkup import InlineKeyboardMarkup
from django_tgbot.types.update import Update

from .bot import state_manager
from .models import TelegramState
from .bot import TelegramBot

from django.conf import settings


logger = logging.getLogger(__name__)


state_manager.set_default_update_types(update_types=update_types.Message)


@processor(state_manager, success='to menu')
def say_hello(bot: TelegramBot, update: Update, state: TelegramState):
    print(state.name)
    logger.info(f'User <{update.get_chat().get_id()}: {update.get_chat().get_username()}> have joined to the bot chat')
    bot.sendMessage(update.get_chat().get_id(), f"Привет {update.get_chat().get_first_name()} {update.get_chat().get_last_name()}!")


@processor(state_manager, from_states='to menu', success='add coast', message_types=message_types.Text, update_types=update_types.Message)
def menu(bot: TelegramBot, update: Update, state: TelegramState):
    if settings.DEBUG:
        logger.info(f'Print menu for user <{update.get_chat().get_id()}: {update.get_chat().get_username()}>')
    print(state.name)
    bot.sendMessage(update.get_chat().get_id(), 'Здесь должно быть меню lorem loremloremloremloremloremloremloremlorem loremloremlorem loremloremloremlorem',
                    # reply_markup=InlineKeyboardMarkup.a(
                    #     inline_keyboard=[
                    #         [InlineKeyboardButton.a('Добавить расход', callback_data='PK'),],
                    #     ]
                    # )
                    )


@processor(state_manager, from_states='add coast', success=state_types.Keep, message_types=message_types.Text, update_types=update_types.Message)
def add_cost(bot: TelegramBot, update: Update, state: TelegramState):
    if settings.DEBUG:
        logger.info(f'')

    bot.sendMessage(update.get_chat().get_id(), f'Введите название расхода')
    cost = update.get_message().get_text()
    bot.sendMessage(update.get_chat().get_id(), f'Вы ввели {cost}')
    bot.sendMessage(update.get_chat().get_id(), f'Введите сумму расхода')
    cost_amount = update.get_message().get_text()
    bot.sendMessage(update.get_chat().get_id(), f'Вы ввели {cost_amount} руб.')
