from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random

# --- محتوای دوره ترک سیگار ---
day_content = {
    "day1": "🚭 روز اول: تصمیم بزرگت رو گرفتی! امروز فقط سیگار نخوری و فکر نکنی بهش. تمرین: لیستی از دلایل ترک سیگار بنویس.",
    # بقیه روزها رو هم بعداً اضافه می‌کنیم (day2 تا day21)
}

# --- جملات انگیزشی ---
motivations = [
    "✨ حتی تاریک‌ترین شب هم با طلوع خورشید تمام می‌شود — و این ترک، طلوع توئه.",
    "🚀 هر بار که به جای سیگار نفس عمیق می‌کشی، بدنت تشکر می‌کنه.",
    "🔥 امروز انتخاب کن قهرمان زندگی خودت باشی، نه قربانی نیکوتین!",
]

# --- فرمان‌ها ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام به ربات ترک سیگار ۲۱ خوش اومدی 👋\n\nبرای شروع می‌تونی از دستورات زیر استفاده کنی:\n/register - ثبت‌نام\n/day1 - شروع روز اول\n/motivate - دریافت پیام انگیزشی"
    )

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"✅ ثبت‌نام انجام شد، {user.first_name} عزیز! آماده‌ای؟ برو سراغ /day1")

async def day1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(day_content["day1"])

async def motivate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote = random.choice(motivations)
    await update.message.reply_text(quote)

# --- اجرای ربات ---

def main():
    app = ApplicationBuilder().token("7964637953:AAE7VsLOZcmIJ80LjFkfazK7gD8pthiIrdc").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("register", register))
    app.add_handler(CommandHandler("day1", day1))
    app.add_handler(CommandHandler("motivate", motivate))

    print("ربات اجرا شد...")
    app.run_polling()

if __name__ == '__main__':
    main()
