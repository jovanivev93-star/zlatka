import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.exceptions import TelegramForbiddenError

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не е поставен во Railway Variables.")

WELCOME_TEXT = (
    "Whatever you saved in 2020 has lost roughly 22% of its purchasing power.\n"
    "Not because of bad decisions.\n"
    "Because inflation quietly changed the math.\n\n"
    "Your account balance went up.\n"
    "Your real buying power didn’t.\n\n"
    "Most retirement accounts are fully exposed to this reality — dependent on paper assets "
    "and a currency that continues to lose value over time.\n\n"
    "That’s why informed retirees think about diversification differently.\n"
    "Not just stocks vs. bonds — but paper vs. tangible.\n\n"
    "Physical gold has preserved purchasing power through every major currency cycle in modern history "
    "because it exists outside the system creating the pressure.\n\n"
    "Augusta Precious Metals helps retirees understand how physical precious metals can be held inside a "
    "tax-advantaged IRA — without penalties or distributions — through a clear, education-first process.\n\n"
    "If you’re curious how this structure works, Augusta offers a free Gold IRA guide that explains the basics "
    "and helps you decide if it’s worth exploring further."
)

BUTTON_TEXT = "See how it works →"
BUTTON_URL = "https://learn.augustapreciousmetals.com/free-guide/?apmtrkr_cid=1696&aff_id=5124"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.chat_join_request()
async def handle_join_request(req: ChatJoinRequest):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=BUTTON_TEXT, url=BUTTON_URL)]
    ])
    try:
        await bot.send_message(req.from_user.id, WELCOME_TEXT, reply_markup=kb)
    except TelegramForbiddenError:
        logging.warning(f"Cannot DM user_id={req.from_user.id} (forbidden).")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
