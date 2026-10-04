import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", "10000"))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📖 Günün aýaty", callback_data="ayat"),
            InlineKeyboardButton("🕌 Günün hadysy", callback_data="hadys"),
        ],
        [
            InlineKeyboardButton("🤲 Dogalar", callback_data="doga"),
            InlineKeyboardButton("📚 Yslam öwren", callback_data="ogren"),
        ],
        [
            InlineKeyboardButton(
                "📢 Yslam Nury kanaly",
                url="https://t.me/yslam_nury50"
            ),
        ],
    ]

    text = (
        "🕌 *Yslam Nury*\n\n"
        "Hoş geldiňiz!\n"
        "Yslam barada peýdaly maglumatlary öwrenmek üçin "
        "aşakdaky bölümlerden birini saýlaň."
    )

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "ayat":
        text = (
            "📖 *Günün aýaty*\n\n"
            "Bu bölümde ygtybarly çeşmelerden aýatlar ýerleşdiriler."
        )

    elif query.data == "hadys":
        text = (
            "🕌 *Günün hadysy*\n\n"
            "Bu bölümde ygtybarly çeşmelerden hadyslar ýerleşdiriler."
        )

    elif query.data == "doga":
        text = (
            "🤲 *Dogalar*\n\n"
            "Bu ýerde dürli dogalary tertipli görnüşde ýerleşdireris."
        )

    elif query.data == "ogren":
        text = (
            "📚 *Yslam öwren*\n\n"
            "Bu bölümde Yslamyň esasy düşünjelerini "
            "ädimme-ädim öwrenip bilersiňiz."
        )

    await query.edit_message_text(
        text,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Baş menýu", callback_data="home")]
        ]),
    )


async def home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton("📖 Günün aýaty", callback_data="ayat"),
            InlineKeyboardButton("🕌 Günün hadysy", callback_data="hadys"),
        ],
        [
            InlineKeyboardButton("🤲 Dogalar", callback_data="doga"),
            InlineKeyboardButton("📚 Yslam öwren", callback_data="ogren"),
        ],
        [
            InlineKeyboardButton(
                "📢 Yslam Nury kanaly",
                url="https://t.me/yslam_nury50"
            ),
        ],
    ]

    await query.edit_message_text(
        "🕌 *Yslam Nury*\n\nBaş menýu:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
    )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN tapylmady!")

    if not WEBHOOK_URL:
        raise RuntimeError("WEBHOOK_URL tapylmady!")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        CallbackQueryHandler(home, pattern="^home$")
    )
    application.add_handler(
        CallbackQueryHandler(buttons)
    )

    print("YslamNuryBot işläp başlady...")

    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path="webhook",
        webhook_url=f"{WEBHOOK_URL}/webhook",
    )


if __name__ == "__main__":
    main()
