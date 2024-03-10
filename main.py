import asyncio
import config
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command
import logging
import random
from Les1.keyboards.keybords import kb1, kb2
from Les1.utils.random_fox import fox
from handlers import common, career_choice

#Асинхронная функция
async def main():
    # Включаем логгирование
    logging.basicConfig(level=logging.INFO)

    # Создаем объект бота
    bot = Bot(token=config.token)

    # Диспечер
    dp = Dispatcher()

    dp.include_router(career_choice.router)
    dp.include_router(common.router)


    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
