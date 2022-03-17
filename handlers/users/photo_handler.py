from aiogram import types
from pathlib import Path

from data.config import BOT_TOKEN
from loader import dp, bot
from utils.getData import toonify


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_image_from_user(message: types.Message):
    message_id = (await message.answer("Yuklanmoqda... 🚀")).message_id
    photo_id = message.photo[-1].file_id
    photo_info = await bot.get_file(photo_id)
    file_path = photo_info['file_path']
    photo_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
    ready_photo = await toonify(photo_url)
    if ready_photo is not None:
        await message.reply_photo(photo=ready_photo)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    else:
        await message.reply("Iltimos yuz qiyofasi aniq ko'ringan rasm yuboring.")

