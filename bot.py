import os
import logging
from pyrogram import Client, filters
import requests

API_TOKEN = os.environ.get("6483542043:AAFw6vDYOhrNQXaMKrl5Z-AXmB-odyF3NXg")  # Make sure this matches the environment variable you set on Heroku

app = Client("my_bot", bot_token=API_TOKEN)

# Start command handler
@app.on_message(filters.command("start"))
async def start_command(client, message):
    mention_html = message.from_user.mention()
    await message.reply_text(
        f"ʜᴇʏ {mention_html} ! 🥳\n\n"
        f"ᴛʜɪs ɪs sᴛxᴛɪɴʏᴜʀʟ ʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ sʜᴏʀᴛ ᴀɴʏ ʟɪɴᴋ ᴜsɪɴɢ ᴛɪɴʏᴜʀʟ ᴀᴘɪ!\n\n"
        f"ᴛᴏ sʜᴏʀᴛ ᴀɴʏ ᴜʀʟ, ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴛʜᴀᴛ ᴜʀʟ ʜᴇʀᴇ ᴀɴᴅ ɪ ᴡɪʟʟ sʜᴏʀᴛ ɪᴛ ғᴏʀ ʏᴏᴜ! 😉"
    )

# URL shortening handler
@app.on_message(filters.regex(r'^https?://'))
async def shorten_url(client, message):
    url = message.text
    try:
        response = requests.get(f'http://tinyurl.com/api-create.php?url={url}')
        short_url = response.text
        await message.reply_text(f"ʜᴇʀᴇ's ᴛʜᴇ sʜᴏʀᴛ ᴜʀʟ:\n{short_url}")
    except Exception as e:
        await message.reply_text("sᴏʀʀʏ, ᴛʜᴇʀᴇ ᴡᴀs ᴀɴ ᴇʀʀᴏʀ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ!")

if __name__ == '__main__':
    app.run()
