import os

from telegram import Update
from validators import url

from Downloader import download_video


# Foydalanuvchi yuborgan URLga video yuborish
async def video_sender(update: Update, text):
    if url(text):
        text = update.message.text.strip()  # Foydalanuvchidan URL olish

        download_path = f'/tmp/{text.split("/")[-1]}.%(ext)s'  # Fayl nomi va saqlash joyi

        # Videoni yuklab olish
        await update.message.reply_text("Yuklab olish boshlandi...")
        await download_video(url, download_path)

        # Video Telegramga yuborish (faylni 'rb' rejimida ochish)
        try:
            with open(download_path, 'rb') as video_file:
                await update.message.reply_video(video_file)
        except Exception as e:
            await update.message.reply_text(f"Xatolik yuz berdi: {str(e)}")

        os.remove(download_path)  # Video yuborilgandan so'ng faylni o'chirish

    else:
        print('Xatolik')
