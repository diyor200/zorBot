import time
from aiogram import types


from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0])
    await message.answer(len(users))


@dp.message_handler(commands="rek", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    text =(await message.from_user.id)
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=ADMINS[0], text=text)
        await time.sleep(1)


@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
