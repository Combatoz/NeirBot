
from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from Les1.keyboards.keybords import kb1, kb2
from Les1.utils.random_fox import fox
from Les1.utils.sovet import sovet

router = Router()

#Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
 name = message.chat.first_name
 await message.answer(f"Привет, {name}", reply_markup=kb1)
 print(message.chat)

@router.message(Command("info"))
async def cmd_info(message: types.Message):
 await message.reply("Я - первый бот COM.bat. В перспективе буду использован для киночата в качестве голосования чатооскара")

@router.message(Command("stop"))
async def cmd_info(message: types.Message):
 name = message.chat.first_name
 await message.reply(f"Пока, {name}")

@router.message(F.text.lower() == "stop!")
async def with_puree(message: types.Message):
 await message.reply("Стоп машина!!")
@router.message(F.text.lower() == "start!")
async def without_puree(message: types.Message):
 await message.reply("Поехали!")
@router.message(F.animation)
async def echo_gif(message: types.Message):
 await message.reply_animation(message.animation.file_id)

@router.message(Command('fox'))
#@dp.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)
    # await bot.send_photo(message.from_user.id, photo=img_fox)

@router.message(Command('sovet'))
#@dp.message(Command('лиса'))
@router.message(F.text.lower() == 'совет')
async def cmd_sovet(message: types.Message):
    name = message.chat.first_name
    img_sovet = sovet()
    await message.answer(f'Твой ответ, {name}')
    await message.answer_animation(animation=img_sovet)


#Хэндлеры на сообщение
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' == msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'инфо' in msg_user:
        await message.answer('Профессия - ненужная фигня, чисто для теста. Можешь пощелкать. Совет - если ты мучаешься каким-то вопросом, просто нажми кнопку и получи ответ. Ювентус и лиса - все очевидно')
    elif 'ювентус' in msg_user:
        await message.reply("Ююююююве сторья ди ун гранде амоооре")
        await message.answer('https://youtu.be/PEhoBkibj6E?si=JE8jdfiN8scMc7mn&t=49')
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')



