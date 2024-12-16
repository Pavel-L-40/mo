from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import api
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboard_crud2 import *
from crud_functions2 import is_included, add_user, show_users

dp = Dispatcher(Bot(token= api), storage = MemoryStorage())

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

@dp.message_handler(text= ['Регистрация'])
async def sing_up(message):
    await message.answer(text= 'Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state= RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username= message.text)
        await message.answer(text= 'Введите свой email: ')
        await RegistrationState.email.set()
    else:
        await message.answer(text= 'Пользователь существует, введите другое имя')
        await sing_up(message)

@dp.message_handler(state= RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email= message.text)
    await message.answer(text= 'Введите свой возраст: ')
    await RegistrationState.age.set()

@dp.message_handler(state= RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age= message.text)
    data_reg = await state.get_data()        # <<--- Получение данных из state
    add_user(data_reg['username'],data_reg['email'], int(data_reg['age']))
    await message.answer(text= f'{data_reg["username"]} успешно добавлен')
    await state.finish()

@dp.message_handler(text= 'all_users')
async def all_users(message):
    list_us = show_users()
    await message.answer(text= list_us)

@dp.message_handler(commands= ['start'])
async def start(message):
    await message.answer(text= 'Регистрация', reply_markup= main_kb)

if __name__ == '__main__':
    executor.start_polling(dp)