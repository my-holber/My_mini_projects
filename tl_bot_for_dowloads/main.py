import json
import os
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import yt_dlp

USERS_FILE = 'users.json'

# Load user data
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save user data
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

# Update user info
def update_user(user_id):
    users = load_users()
    now = datetime.now().isoformat()
    if user_id in users:
        users[user_id]['last_used'] = now
        users[user_id]['count'] += 1
    else:
        users[user_id] = {'last_used': now, 'count': 1}
    save_users(users)

# Download video
def download_video(url, output_path='downloads/'):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_file = ydl.prepare_filename(info_dict)
        return video_file

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Здравствуйте! Отправьте мне ссылку на TikTok или YouTube, и я загружу видео для вас.')

# Handle text messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.message.from_user.id)
    url = update.message.text
    await update.message.reply_text('Загрузка...')
    
    update_user(user_id)  # Update user info

    try:
        video_file = download_video(url)
        await update.message.reply_text('Загрузка завершена! Вот ваше видео:')
        with open(video_file, 'rb') as video:
            await update.message.reply_video(video=video)
        os.remove(video_file)  # Remove the video after sending
    except yt_dlp.utils.DownloadError:
        await update.message.reply_text('Произошла ошибка при загрузке видео. Пожалуйста, проверьте ссылку и попробуйте еще раз.')
    except Exception as e:
        await update.message.reply_text('Произошла ошибка. Пожалуйста, попробуйте позже.')

def main() -> None:
    # Replace with your bot token
    application = ApplicationBuilder().token("YOU_TOKEN").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    main()
