from video_sender import video_sender

async def message_handler(update, context):
    text = update.message.text
    user = update.effective_user

    if text:
        await video_sender(update, text)

    else:
        await context.bot.send_message(text="<b>Video url yuboring!</b>", chat_id=user.id, parse_mode='HTML')

