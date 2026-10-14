import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8844901417:AAF4lXCGQniDXMK0qAIpqUbNnlnzH-UdUjE"
CHANNEL_IDS = [-1003759272525, -1003769057593, -1003799225915]

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا! دزلي ملف حتى اوزعه على قنواتك الـ 3")

async def distribute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    for cid in CHANNEL_IDS:
        try:
            if msg.text:
                await context.bot.send_message(cid, msg.text)
            elif msg.photo:
                await context.bot.send_photo(cid, msg.photo[-1].file_id, caption=msg.caption)
            elif msg.video:
                await context.bot.send_video(cid, msg.video.file_id, caption=msg.caption)
            elif msg.audio:
                await context.bot.send_audio(cid, msg.audio.file_id, caption=msg.caption)
            elif msg.document:
                await context.bot.send_document(cid, msg.document.file_id, caption=msg.caption)
        except Exception as e:
            print(f"Error {cid}: {e}")
    await msg.reply_text("تم التوزيع على 3 قنوات ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, distribute))
print("Bot started...")
app.run_polling()
