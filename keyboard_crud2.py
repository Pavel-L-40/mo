from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(resize_keyboard= True)
button_reg = KeyboardButton(text= 'Регистрация')
button_all_us = KeyboardButton(text= 'all_users')
main_kb.add(button_reg,button_all_us)