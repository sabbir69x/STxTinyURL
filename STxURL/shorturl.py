import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import requests

API_TOKEN = '6483542043:AAFw6vDYOhrNQXaMKrl5Z-AXmB-odyF3NXg'  # Replace with your actual bot API token
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
logging.getLogger(__name__)

# Start command handler
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    mention_html = md.quote_html(message.from_user.mention)
    await message.reply(f"ʜᴇʏ {mention_html} ! 🥳\n\n"
                        f"ᴛʜɪs ɪs sᴛxᴛɪɴʏᴜʀʟ ʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ sʜᴏʀᴛ ᴀɴʏ ʟɪɴᴋ ᴜsɪɴɢ ᴛɪɴʏᴜʀʟ ᴀᴘɪ!\n\n"
                        f"ᴛᴏ sʜᴏʀᴛ ᴀɴʏ ᴜʀʟ, ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴛʜᴀᴛ ᴜʀʟ ʜᴇʀᴇ ᴀɴᴅ ɪ ᴡɪʟʟ sʜᴏʀᴛ ɪᴛ ғᴏʀ ʏᴏᴜ! 😉")

# URL shortening handler
@dp.message_handler(lambda message: message.text.startswith('http'))
async def shorten_url(message: types.Message):
    url = message.text.strip()
    try:
        response = requests.get(f'http://tinyurl.com/api-create.php?url={url}')
        short_url = response.text
        await message.reply(f"ʜᴇʀᴇ's ᴛʜᴇ sʜᴏʀᴛ ᴜʀʟ:\n{short_url}")
    except Exception as e:
        await message.reply("sᴏʀʀʏ, ᴛʜᴇʀᴇ ᴡᴀs ᴀɴ ᴇʀʀᴏʀ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ!")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
