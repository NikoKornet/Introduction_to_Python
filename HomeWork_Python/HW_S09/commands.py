from config import dp, bot
from aiogram import types
from keyboards import menu_buttons, players_move
import random

total = 0


@dp.message_handler(commands=['start', 'info'])
async def start_bot(message: types.Message):
    print(message)
    await message.reply(f'Привет, {message.from_user.first_name}!')
    print('start')
    await message.answer("/info - справка по командам, /play - сыграть в игру")
    await message.reply('Выбирай!', reply_markup=menu_buttons.kb_menu)


@dp.message_handler(commands='play')
async def game_start_bot(message: types.Message):
    global total
    total = 150
    await message.reply(
        f'Привет, {message.from_user.first_name}! На столе лежит {total} конфет.\nЗа раз можно взять от 1 до 28.\nПобеждает тот кто взял последнюю.')
    await message.answer('Кто ходит?', reply_markup=players_move.kb_players)


@dp.message_handler(commands=['Я', 'Бот'])
async def player_moves(message: types.Message):
    global total
    total = 150
    players = ['Я', 'Бот']
    if message.text[1:] == "Я":
        await message.reply(f'Ты ходишь первым {message.from_user.first_name}!')
    else:
        await message.reply(f'{message.from_user.first_name}, первым ходит Бот!')
        bot_move = random.randint(1, 28)
        total -= bot_move
        await message.answer(f'Бот взял {bot_move} конфет и осталось {total}.')


@dp.message_handler()
async def play_candy_bot(message: types.Message):
    global total
    if message.text.isdigit():
        if total <= 0:
            await message.reply(f'{message.from_user.first_name}, '
                                f'игра закончена! Хочешь, сыграть пиши /play')
        else:
            take = int(message.text)
            print(f'{message.from_user.first_name} взял {take}.')

            if take < 1 or take > 28 or take > total:
                await message.reply(f'{message.from_user.first_name}, не верный ход!')
            else:
                total -= take
                if total == 0:
                    await message.reply(f'{message.from_user.first_name}, '
                                        f'взял {take} конфет и осталось {total}.')
                    await message.answer(f'{message.from_user.first_name}, выиграл!')
                    await message.reply('Хочешь еще раз?', reply_markup=menu_buttons.kb_menu)
                else:
                    await message.reply(f'{message.from_user.first_name}, '
                                        f'взял {take} конфет и осталось {total}.')
                    bot_move = 0
                    if total < 29:
                        bot_move = total
                    else:
                        bot_move = random.randint(1, 28)
                    total -= bot_move
                    if total == 0:
                        await message.answer(f'Бот взял {bot_move} конфет и осталось {total}.')
                        await message.answer('Бот выиграл!')
                        await message.reply('Хочешь еще раз?', reply_markup=menu_buttons.kb_menu)
                    else:
                        await message.answer(f'Бот взял {bot_move} конфет и осталось {total}.')
    else:
        await message.reply(f'{message.from_user.first_name}, введите количество:')


@dp.message_handler()
async def all_bot(message: types.Message):
    print(message)
    print('All')
    await message.reply(f'{message.from_user.first_name}, хочешь сыграть! Пиши /play')
