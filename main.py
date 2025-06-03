from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# সরাসরি টোকেন সেট (শুধুমাত্র ডেমো বা টেস্টিং এর জন্য)
BOT_TOKEN = "7821218866:AAFxPSzZj_NwPworHHyUrY20Oo0THMfwLOg"

# /start কমান্ডে ফোন নম্বর চাওয়ার বাটন
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact_button = KeyboardButton(text="📱 আমার ফোন নম্বর শেয়ার করুন", request_contact=True)
    reply_markup = ReplyKeyboardMarkup([[contact_button]], resize_keyboard=True, one_time_keyboard=True)

    await update.message.reply_text("অনুগ্রহ করে আপনার ফোন নম্বর শেয়ার করুন:", reply_markup=reply_markup)

# ফোন নম্বর পাওয়া গেলে
async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact

    phone_number = contact.phone_number
    user_id = contact.user_id
    first_name = contact.first_name

    message = f"✅ ধন্যবাদ {first_name}!\n\n📞 আপনার ফোন নম্বর: {phone_number}\n🆔 Telegram ID: {user_id}"
    await update.message.reply_text(message)

    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(f"{first_name} | {user_id} | {phone_number}\n")

# অ্যাপ রান করা
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.CONTACT, contact_handler))

app.run_polling()
