import asyncio
import yt_dlp
from telegram import Update



# Asenkron video yuklab olish funksiyasi
async def download_video(url, download_path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Eng yuqori sifatdagi video va audio
        'outtmpl': download_path,  # Fayl saqlanadigan joy
        'quiet': True  # Ogohlantirishlarni o'chirish
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    await asyncio.to_thread(ydl.download, [url])  # Asenkron tarzda yuklab olish


# Parallel ravishda bir nechta URLni yuklab olish
async def handle_multiple_urls(update: Update, context):
    urls = update.message.text.split()  # Bir nechta URLlarni olish
    tasks = []  # Parallel yuklab olish vazifalari uchun ro'yxat

    # Har bir URL uchun yuklab olish vazifasini yaratish
    for url in urls:
        download_path = f'/tmp/{url.split("/")[-1]}.%(ext)s'
        tasks.append(download_video(url, download_path))

    # Barcha yuklab olishlarni parallel bajarish
    await asyncio.gather(*tasks)

    # Foydalanuvchiga muvaffaqiyatli javob berish
    await update.message.reply_text("Barcha videolar yuklab olindi va yuborildi!")






