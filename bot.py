import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

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
            InlineKeyboardButton("📢 Yslam Nury kanaly", url="https://t.me/yslam_nury50"),
        ],
    ]

    text = (
        "🕌 *Yslam Nury*\n\n"
        "Hoş geldiňiz!\n"
        "Yslam barada peýdaly maglumatlary öwrenmek üçin aşakdaky bölümlerden birini saýlaň."
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
        text = "📖 *Günün aýaty*\n\nBu bölüme soňra ygtybarly çeşmelerden aýatlar goşarys."

    elif query.data == "hadys":
        text = "🕌 *Günün hadysy*\n\nBu bölüme soňra ygtybarly çeşmelerden hadyslar goşarys."

    elif query.data == "doga":
        text = "🤲 *Dogalar*\n\nBu ýerde dürli dogalary tertipli görnüşde ýerleşdireris."

    elif query.data == "ogren":
        text = "📚 *Yslam öwren*\n\nBu bölümde Yslamyň esasy düşünjelerini ädimme-ädim öwrenip bilersiňiz."

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
            InlineKeyboardButton("📢 Yslam Nury kanaly", url="https://t.me/yslam_nury50"),
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

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(home, pattern="^home$"))
    app.add_handler(CallbackQueryHandler(buttons))

    print("YslamNuryBot işläp başlady...")
    app.run_polling()


if __name__ == "__main__":
    main()
