import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

bughunter0 = Client(
    "Ban-Bot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)

 if message.reply_to_message:
  admins = await bot.get_chat_members(chat_id=chatid, filter="administrators")
  userid = message.from_user.id
  if userid in admins:    
    chatid = message.chat.id
    user_to_ban = message.reply_to_message.from_user.id
    if user_to_ban in admins:
        await message.reply(text="Think he is Admin, Can't Ban Admins")   
    else:
        try:  
            await bot.kick_chat_member(chat_id=chatid, user_id=user_to_ban)
        except Exception as error:
            await message.reply_text(f"{error")
  else:
      await message.reply_text("Nice try, But wrong move..")
      return
 else:
    return
