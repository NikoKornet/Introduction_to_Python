from aiogram import types, Dispatcher

import commands


def registered_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_bot, commands=['start', 'info'])
    dp.register_message_handler(commands.game_start_bot, commands='play')
    dp.register_message_handler(commands.player_moves, commands=['Я', 'Бот'])
    dp.register_message_handler(commands.play_candy_bot)
    dp.register_message_handler(commands.all_bot)