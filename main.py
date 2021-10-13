
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


@bughunter0.on_message(filters.command(["ban"]))
async def ban(bot, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user = await bot.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    if user.can_restrict_members is False:
        await message.reply_text(
            text="You can't do that!"
        )
        return
    if message.reply_to_message:
        user_to_ban_id = message.reply_to_message.from_user.id
    else:
        if len(message.text.split()) > 1:
            user_to_ban_id = message.text.split()[1]  # you can ban with "/ban id"
        else:
            await message.reply_text(
                text="Send command with id of user to ban."
            )
            return
    user_to_ban = await bot.get_chat_member(
        chat_id=chat_id,
        user_id=user_to_ban_id
    )
    if user_to_ban.status == "administrator":
        await message.reply(
            text="He is an admin of this chat, So I can't ban admins."
        )
    else:
        try:
            await bot.kick_chat_member(chat_id=chatid, user_id=user_to_ban_id)
            await message.reply_text(
                text=f"Banned {message.reply_to_message.from_user.mention}!"
            )
        except Exception as error:
            await message.reply_text(error)


bughunter0.run()

