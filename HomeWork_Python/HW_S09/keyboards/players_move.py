from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button3 = KeyboardButton('/Я')
button4 = KeyboardButton('/Бот')

kb_players = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_players.add(button3).insert(button4)