import requests

from Downloader import download_instagram_media


async def send_video(update, context):
    url = update.message.text.strip()  # Foydalanuvchidan URL olish

    if not url:
        await update.message.reply_text("Iltimos, Instagram URL yuboring.")
        return

    await update.message.reply_text("Instagram media yuklanmoqda...")

    try:
        # Instagramdan barcha media fayllarni olish
        media_files = await download_instagram_media(url)

        # Har bir media faylni foydalanuvchiga yuborish
        for media_url, media_type in media_files:
            response = requests.get(media_url, stream=True)
            if media_type == 'video/mp4':
                await update.message.reply_video(response.content)
            else:
                await update.message.reply_photo(response.content)


    except Exception as e:
        await update.message.reply_text(f"Xatolik yuz berdi: {str(e)}")
