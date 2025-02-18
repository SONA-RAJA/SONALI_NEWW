from SONALI_MUSIC import app
from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated

@app.on_chat_member_updated()
async def video_chat_event(client, update: ChatMemberUpdated):
    # चेक करें कि क्या सदस्य वीडियो चैट में जुड़ा है
    if update.new_chat_member and update.new_chat_member.status == "member":
        # वीडियो चैट प्रिविलेज चेक करें
        if update.new_chat_member.privileges and update.new_chat_member.privileges.can_manage_video_chats:
            user = update.new_chat_member.user
            chat_id = update.chat.id
            mention = f"[{user.first_name}](tg://user?id={user.id})"
            username = f"@{user.username}" if user.username else "No Username"
            user_id = user.id

            message = f"🎥 **New User Joined Video Chat**\n\n👤 Name: {mention}\n🆔 User ID: `{user_id}`\n🔗 Username: {username}"
            
            await client.send_message(chat_id, message)
