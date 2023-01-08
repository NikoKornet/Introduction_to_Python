from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
button1 = KeyboardButton('/info')
button2 = KeyboardButton('/play')

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.row(button1, button2)