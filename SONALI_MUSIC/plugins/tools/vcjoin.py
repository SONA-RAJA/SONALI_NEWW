from SONALI_MUSIC import app
from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated

@app.on_chat_member_updated()
async def video_chat_event(client, update: ChatMemberUpdated):
    # चेक करें कि सदस्य ने वीडियो चैट जॉइन किया है
    if update.new_chat_member and update.new_chat_member.status == "member":
        # चेक करें कि क्या वह वीडियो चैट में जुड़ा है
        if update.new_chat_member.user:
            user = update.new_chat_member.user
            chat_id = update.chat.id
            mention = f"[{user.first_name}](tg://user?id={user.id})"
            username = f"@{user.username}" if user.username else "No Username"
            user_id = user.id

            # वीडियो चैट में जुड़ने की जानकारी भेजें
            message = f"🎥 **User Joined Video Chat**\n\n👤 Name: {mention}\n🆔 User ID: `{user_id}`\n🔗 Username: {username}"
            
            await client.send_message(chat_id, message)
