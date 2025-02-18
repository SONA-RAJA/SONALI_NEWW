from pyrogram import Client, filters
from SONALI_MUSIC import app
from pyrogram.types import ChatMemberUpdated

@app.on_video_chat_participant_joined()
async def video_chat_participant_joined(client, update):
    user = update.user
    chat_id = update.chat.id
    mention = f"[{user.first_name}](tg://user?id={user.id})"
    username = f"@{user.username}" if user.username else "No Username"
    user_id = user.id

    # वीडियो चैट में जुड़ने की जानकारी भेजें
    message = f"🎥 **New User Joined Video Chat**\n\n👤 Name: {mention}\n🆔 User ID: `{user_id}`\n🔗 Username: {username}"
    
    await client.send_message(chat_id, message)
