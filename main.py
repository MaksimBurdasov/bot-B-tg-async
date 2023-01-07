import logging
from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def inline_keyboard_maker():
    # создание клавиатуры
    kb = types.InlineKeyboardMarkup(row_width=3)

    # описание данных, которые будут указаны при создании кнопок клавиатуры
    text_and_data = (
        ('Goodness', 'goodness'),
        ('Evil', 'evil')
    )

    # создание кнопок
    row_buttons = []  # список кнопок
    for text, data in text_and_data:
        row_buttons.append(types.InlineKeyboardButton(text, callback_data=data))

    # добавление кнопок к клавиатуре
    kb.row(*row_buttons)

    return kb


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=inline_keyboard_maker())


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
