import json
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)


with open("verses.json", "r", encoding="utf-8") as f:
    VERSES = json.load(f)


with open("encouragements.json", "r", encoding="utf-8") as f:
    ENCOURAGEMENTS = json.load(f)


def full_mood_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("😊 Happy", callback_data="happy"),
            InlineKeyboardButton("😔 Sad", callback_data="sad")
        ],
        [
            InlineKeyboardButton("😟 Anxious", callback_data="anxious"),
            InlineKeyboardButton("🙏 Thankful", callback_data="thankful")
        ],
        [
            InlineKeyboardButton("😴 Tired", callback_data="tired")
        ]
    ])


def small_verse_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔄 Choose another mood", callback_data="choose_again"),
            InlineKeyboardButton("🙏 Thank you", callback_data="thank_you")
        ]
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello 👋\nHow are you feeling today?",
        reply_markup=full_mood_keyboard()
    )


async def mood_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "choose_again":
        await query.message.reply_text(
            "Choose your mood:",
            reply_markup=full_mood_keyboard()
        )
        return

    if query.data == "thank_you":
        
        messages_to_send = [random.choice(ENCOURAGEMENTS)]
        for msg in messages_to_send:
            await query.message.reply_text(msg)
        return

    
    mood = query.data
    verse = random.choice(VERSES[mood])

    await query.message.reply_text(
        f"📖 {verse}",
        reply_markup=small_verse_keyboard()
    )


if __name__ == "__main__":
    TOKEN = "8045500304:AAHRj91UAjkCNp-qFjuKZBD3STNWf1sId9E"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(mood_button))

    print("Bible Mood Bot is running...")
    app.run_polling()
