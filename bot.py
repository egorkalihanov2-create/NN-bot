import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton,
    ReplyKeyboardRemove, MessageEntity
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "8754884801:AAH6fK1yb74lrdQ3z-Qe6GbB5gWKqGDZw0k"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ─── file_ids ────────────────────────────────────────────────────────────────

STICKER_4  = "CAACAgIAAxkBAAFKNMxqDlYLCxlmwdrIi9R1OM0tzBpHfgACtp4AAv6pcUjIBM5zPdRHSzsE"
STICKER_6  = "CAACAgIAAxkBAAFKNNBqDlYhnLN3zPTHtErQJEnw2-_IVQACXZEAAmvCCUq36dINQzXCDTsE"
STICKER_12 = "CAACAgIAAxkBAAFKNO1qDlfXMey4RPdl3GlbXX_elAUeKQACnpoAAnCxcEg5g3RsiScu3zsE"

PHOTO_8_UZHAS = "https://raw.githubusercontent.com/egorkalihanov2-create/NN-bot/main/pics/uzhasword.png"
PHOTO_8_UGAR  = "https://raw.githubusercontent.com/egorkalihanov2-create/NN-bot/main/pics/ugarword.png"
PHOTO_10      = "https://raw.githubusercontent.com/egorkalihanov2-create/NN-bot/main/pics/signal.png"
PHOTO_11      = "https://raw.githubusercontent.com/egorkalihanov2-create/NN-bot/main/pics/boys.png"
PHOTO_13      = "https://raw.githubusercontent.com/egorkalihanov2-create/NN-bot/main/pics/book.png"

# ─── helpers ─────────────────────────────────────────────────────────────────

def E(spec: list) -> list[MessageEntity]:
    result = []
    for s in spec:
        kwargs = {"type": s["type"], "offset": s["offset"], "length": s["length"]}
        if s.get("custom_emoji_id"):
            kwargs["custom_emoji_id"] = s["custom_emoji_id"]
        result.append(MessageEntity(**kwargs))
    return result

# ─── тексты ──────────────────────────────────────────────────────────────────

K = "\U0001F5DD"  # 🗝 — кастомный эмодзи-заглушка (реальный id ниже)

MSG1_TEXT = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD фух! ну и история, бро!\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "об этом надо написать книгу!"
)
MSG1_ENT = [
    {"offset":0,"length":44,"type":"blockquote"},
    {"offset":0,"length":2,"type":"custom_emoji","custom_emoji_id":"5220121337665726730"},
    {"offset":2,"length":2,"type":"custom_emoji","custom_emoji_id":"5220025809003130352"},
    {"offset":4,"length":2,"type":"custom_emoji","custom_emoji_id":"5219901499764678745"},
    {"offset":7,"length":2,"type":"custom_emoji","custom_emoji_id":"5221978279661049220"},
    {"offset":9,"length":2,"type":"custom_emoji","custom_emoji_id":"5219803776373790987"},
    {"offset":11,"length":2,"type":"custom_emoji","custom_emoji_id":"5219780991572286175"},
    {"offset":38,"length":2,"type":"custom_emoji","custom_emoji_id":"5222411637566247305"},
    {"offset":40,"length":2,"type":"custom_emoji","custom_emoji_id":"5219960315046830005"},
    {"offset":42,"length":2,"type":"custom_emoji","custom_emoji_id":"5219951742292109016"},
    {"offset":45,"length":28,"type":"blockquote"},
]

MSG2_TEXT = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD эээ? давай без вопросов...\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "берись за ручку!"
)
MSG2_ENT = [
    {"offset":0,"length":47,"type":"blockquote"},
    {"offset":0,"length":2,"type":"custom_emoji","custom_emoji_id":"5220138654973862915"},
    {"offset":2,"length":2,"type":"custom_emoji","custom_emoji_id":"5220203766678068592"},
    {"offset":4,"length":2,"type":"custom_emoji","custom_emoji_id":"5220091818355499138"},
    {"offset":7,"length":2,"type":"custom_emoji","custom_emoji_id":"5220069613374579574"},
    {"offset":9,"length":2,"type":"custom_emoji","custom_emoji_id":"5219958725908930395"},
    {"offset":11,"length":2,"type":"custom_emoji","custom_emoji_id":"5219898776755412740"},
    {"offset":41,"length":2,"type":"custom_emoji","custom_emoji_id":"5220028501947623425"},
    {"offset":43,"length":2,"type":"custom_emoji","custom_emoji_id":"5220131825975862523"},
    {"offset":45,"length":2,"type":"custom_emoji","custom_emoji_id":"5220061650505214423"},
    {"offset":48,"length":16,"type":"blockquote"},
]

MSG3_TEXT = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD я задам темп, а ты продолжай\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "это был обычный летний день..."
)
MSG3_ENT = [
    {"offset":0,"length":49,"type":"blockquote"},
    {"offset":0,"length":2,"type":"custom_emoji","custom_emoji_id":"5220121337665726730"},
    {"offset":2,"length":2,"type":"custom_emoji","custom_emoji_id":"5220025809003130352"},
    {"offset":4,"length":2,"type":"custom_emoji","custom_emoji_id":"5219901499764678745"},
    {"offset":7,"length":2,"type":"custom_emoji","custom_emoji_id":"5221978279661049220"},
    {"offset":9,"length":2,"type":"custom_emoji","custom_emoji_id":"5219803776373790987"},
    {"offset":11,"length":2,"type":"custom_emoji","custom_emoji_id":"5219780991572286175"},
    {"offset":43,"length":2,"type":"custom_emoji","custom_emoji_id":"5222411637566247305"},
    {"offset":45,"length":2,"type":"custom_emoji","custom_emoji_id":"5219960315046830005"},
    {"offset":47,"length":2,"type":"custom_emoji","custom_emoji_id":"5219951742292109016"},
    {"offset":50,"length":30,"type":"blockquote"},
]

MSG5_TEXT = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD чувак, да мы как братья грим!\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "но в гриме только я, да и не братья\u2026 не суть, бро! пока не разогнались, давай-ка я наберу знакомому дизайнеру - пусть глянет на наши труды"
)
MSG5_ENT = [
    {"offset":0,"length":50,"type":"blockquote"},
    {"offset":0,"length":2,"type":"custom_emoji","custom_emoji_id":"5220138654973862915"},
    {"offset":2,"length":2,"type":"custom_emoji","custom_emoji_id":"5220203766678068592"},
    {"offset":4,"length":2,"type":"custom_emoji","custom_emoji_id":"5220091818355499138"},
    {"offset":7,"length":2,"type":"custom_emoji","custom_emoji_id":"5220069613374579574"},
    {"offset":9,"length":2,"type":"custom_emoji","custom_emoji_id":"5219958725908930395"},
    {"offset":11,"length":2,"type":"custom_emoji","custom_emoji_id":"5219898776755412740"},
    {"offset":44,"length":2,"type":"custom_emoji","custom_emoji_id":"5220028501947623425"},
    {"offset":46,"length":2,"type":"custom_emoji","custom_emoji_id":"5220131825975862523"},
    {"offset":48,"length":2,"type":"custom_emoji","custom_emoji_id":"5220061650505214423"},
    {"offset":51,"length":138,"type":"blockquote"},
]

MSG7_TEXT = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DDпривет! что тут у вас? \n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD братаан! ты офигеешь!\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD"
)
MSG7_ENT = [
    {"offset":0,"length":43,"type":"blockquote"},
    {"offset":0,"length":2,"type":"custom_emoji","custom_emoji_id":"5220138654973862915"},
    {"offset":2,"length":2,"type":"custom_emoji","custom_emoji_id":"5220203766678068592"},
    {"offset":4,"length":2,"type":"custom_emoji","custom_emoji_id":"5220091818355499138"},
    {"offset":7,"length":2,"type":"custom_emoji","custom_emoji_id":"5219785995209185967"},
    {"offset":9,"length":2,"type":"custom_emoji","custom_emoji_id":"5219935490135860144"},
    {"offset":11,"length":2,"type":"custom_emoji","custom_emoji_id":"5219909690267312927"},
    {"offset":37,"length":2,"type":"custom_emoji","custom_emoji_id":"5219944539631949923"},
    {"offset":39,"length":2,"type":"custom_emoji","custom_emoji_id":"5219750793657226454"},
    {"offset":41,"length":2,"type":"custom_emoji","custom_emoji_id":"5222207540720343242"},
    {"offset":44,"length":42,"type":"blockquote"},
    {"offset":44,"length":2,"type":"custom_emoji","custom_emoji_id":"5220138654973862915"},
    {"offset":46,"length":2,"type":"custom_emoji","custom_emoji_id":"5220203766678068592"},
    {"offset":48,"length":2,"type":"custom_emoji","custom_emoji_id":"5220091818355499138"},
    {"offset":51,"length":2,"type":"custom_emoji","custom_emoji_id":"5219944539631949923"},
    {"offset":53,"length":2,"type":"custom_emoji","custom_emoji_id":"5219750793657226454"},
    {"offset":55,"length":2,"type":"custom_emoji","custom_emoji_id":"5222207540720343242"},
    {"offset":80,"length":2,"type":"custom_emoji","custom_emoji_id":"5220138654973862915"},
    {"offset":82,"length":2,"type":"custom_emoji","custom_emoji_id":"5220203766678068592"},
    {"offset":84,"length":2,"type":"custom_emoji","custom_emoji_id":"5220091818355499138"},
]

MSG8_CAPTION = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\u0439\u043e\u0443\u2026 \u043a\u0430\u043a \u0431\u044b \u043f\u043e\u043c\u044f\u0433\u0447\u0435\u2026\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\u0434\u0430\u0432\u0430\u0439 \u043f\u0440\u0438\u043a\u0438\u043d\u0435\u043c, \u043a\u0430\u043a \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u0433\u043b\u044f\u0434\u0435\u0442\u044c \u0442\u0435\u043a\u0441\u0442, \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u0438 \u043f\u0440\u043e\u0447\u0435\u0435\u2026"
)
MSG8_ENT = [
    {"offset":0,"length":40,"type":"blockquote"},
    {"offset":0,"length":2,"type":"custom_emoji","custom_emoji_id":"5220138654973862915"},
    {"offset":2,"length":2,"type":"custom_emoji","custom_emoji_id":"5220203766678068592"},
    {"offset":4,"length":2,"type":"custom_emoji","custom_emoji_id":"5220091818355499138"},
    {"offset":7,"length":2,"type":"custom_emoji","custom_emoji_id":"5219785995209185967"},
    {"offset":9,"length":2,"type":"custom_emoji","custom_emoji_id":"5219935490135860144"},
    {"offset":11,"length":2,"type":"custom_emoji","custom_emoji_id":"5219909690267312927"},
    {"offset":34,"length":2,"type":"custom_emoji","custom_emoji_id":"5219944539631949923"},
    {"offset":36,"length":2,"type":"custom_emoji","custom_emoji_id":"5219750793657226454"},
    {"offset":38,"length":2,"type":"custom_emoji","custom_emoji_id":"5222207540720343242"},
    {"offset":41,"length":71,"type":"blockquote"},
]

MSG9_TEXT = "(далее — посты в хронологическом порядке, которые дропнутся разом. без интерактива. сорри.)"

MSG10_CAPTION = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD \u0441\u0442\u044d\u043d\u0434 \u0430\u043f!\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\u0441\u0438\u0433\u043d\u0430\u043b \u043e\u0442\u043f\u0435\u0447\u0430\u0442\u0430\u043b\u0438!"
)
MSG10_ENT = [
    {"offset":0,"length":30,"type":"blockquote"},
    {"offset":0,"length":2,"type":"custom_emoji","custom_emoji_id":"5220121337665726730"},
    {"offset":2,"length":2,"type":"custom_emoji","custom_emoji_id":"5220025809003130352"},
    {"offset":4,"length":2,"type":"custom_emoji","custom_emoji_id":"5219901499764678745"},
    {"offset":7,"length":2,"type":"custom_emoji","custom_emoji_id":"5221978279661049220"},
    {"offset":9,"length":2,"type":"custom_emoji","custom_emoji_id":"5219803776373790987"},
    {"offset":11,"length":2,"type":"custom_emoji","custom_emoji_id":"5219780991572286175"},
    {"offset":24,"length":2,"type":"custom_emoji","custom_emoji_id":"5222411637566247305"},
    {"offset":26,"length":2,"type":"custom_emoji","custom_emoji_id":"5219960315046830005"},
    {"offset":28,"length":2,"type":"custom_emoji","custom_emoji_id":"5219951742292109016"},
    {"offset":31,"length":18,"type":"blockquote"},
]

MSG11_CAPTION = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD \u0437\u0430\u0445\u043e\u0434\u0438 \u0441\u043f\u0440\u0430\u0432\u0430!\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\u0443 \u043d\u0435\u0433\u043e \u043e\u0442\u0446\u0435\u043d\u0442\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0435 \u0437\u0440\u0435\u043d\u0438\u0435!"
)
MSG11_ENT = [
    {"offset":0,"length":35,"type":"blockquote"},
    {"offset":0,"length":2,"type":"custom_emoji","custom_emoji_id":"5220121337665726730"},
    {"offset":2,"length":2,"type":"custom_emoji","custom_emoji_id":"5220025809003130352"},
    {"offset":4,"length":2,"type":"custom_emoji","custom_emoji_id":"5219901499764678745"},
    {"offset":7,"length":2,"type":"custom_emoji","custom_emoji_id":"5221978279661049220"},
    {"offset":9,"length":2,"type":"custom_emoji","custom_emoji_id":"5219803776373790987"},
    {"offset":11,"length":2,"type":"custom_emoji","custom_emoji_id":"5219780991572286175"},
    {"offset":28,"length":2,"type":"custom_emoji","custom_emoji_id":"5222411637566247305"},
    {"offset":30,"length":2,"type":"custom_emoji","custom_emoji_id":"5219960315046830005"},
    {"offset":32,"length":2,"type":"custom_emoji","custom_emoji_id":"5219951742292109016"},
    {"offset":36,"length":29,"type":"blockquote"},
]

MSG13_CAPTION = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD \u0434\u0430\u0439 \u043f\u0440\u0430\u0432\u043a\u0438 \u0442\u0438\u043f\u043e\u0433\u0440\u0430\u0444\u0438\u0438\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD"
)
MSG13_ENT = [
    {"offset":0,"length":42,"type":"blockquote"},
    {"offset":0,"length":2,"type":"custom_emoji","custom_emoji_id":"5220121337665726730"},
    {"offset":2,"length":2,"type":"custom_emoji","custom_emoji_id":"5220025809003130352"},
    {"offset":4,"length":2,"type":"custom_emoji","custom_emoji_id":"5219901499764678745"},
    {"offset":7,"length":2,"type":"custom_emoji","custom_emoji_id":"5221978279661049220"},
    {"offset":9,"length":2,"type":"custom_emoji","custom_emoji_id":"5219803776373790987"},
    {"offset":11,"length":2,"type":"custom_emoji","custom_emoji_id":"5219780991572286175"},
    {"offset":27,"length":2,"type":"custom_emoji","custom_emoji_id":"5222411637566247305"},
    {"offset":29,"length":2,"type":"custom_emoji","custom_emoji_id":"5219960315046830005"},
    {"offset":31,"length":2,"type":"custom_emoji","custom_emoji_id":"5219951742292109016"},
]

# ─── keyboards ────────────────────────────────────────────────────────────────

def kb_start() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="что за история?"), KeyboardButton(text="погнали!")]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

def kb_scenario() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="этот ужас...", callback_data="scenario_uzhas")
    b.button(text="такой угар!", callback_data="scenario_ugar")
    b.adjust(2)
    return b.as_markup()

def kb_book() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="1", callback_data="book_1")
    b.button(text="2", callback_data="book_2")
    b.button(text="3", callback_data="book_3")
    b.adjust(3)
    return b.as_markup()

# ─── flow functions ───────────────────────────────────────────────────────────

async def send_msg3_then_sticker4(chat_id: int):
    await bot.send_message(chat_id, MSG3_TEXT, entities=E(MSG3_ENT), reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(3)
    await bot.send_sticker(chat_id, STICKER_4, reply_markup=kb_scenario())

async def continue_after_scenario(chat_id: int, chosen: str):
    try:
        await asyncio.sleep(5)
        logger.info(f"[{chat_id}] sending msg5")
        await bot.send_message(chat_id, MSG5_TEXT, entities=E(MSG5_ENT))

        await asyncio.sleep(2)
        logger.info(f"[{chat_id}] sending sticker6")
        await bot.send_sticker(chat_id, STICKER_6)

        await asyncio.sleep(3)
        logger.info(f"[{chat_id}] sending msg7")
        await bot.send_message(chat_id, MSG7_TEXT, entities=E(MSG7_ENT))

        logger.info(f"[{chat_id}] sending msg8 ({chosen})")
        photo_id = PHOTO_8_UZHAS if chosen == "uzhas" else PHOTO_8_UGAR
        await bot.send_photo(chat_id, photo_id, caption=MSG8_CAPTION, caption_entities=E(MSG8_ENT))

        await asyncio.sleep(10)
        logger.info(f"[{chat_id}] sending msg9")
        await bot.send_message(chat_id, MSG9_TEXT)

        await asyncio.sleep(2)
        logger.info(f"[{chat_id}] sending msg10")
        await bot.send_photo(chat_id, PHOTO_10, caption=MSG10_CAPTION, caption_entities=E(MSG10_ENT))

        await asyncio.sleep(5)
        logger.info(f"[{chat_id}] sending msg11")
        await bot.send_photo(chat_id, PHOTO_11, caption=MSG11_CAPTION, caption_entities=E(MSG11_ENT))

        await asyncio.sleep(5)
        logger.info(f"[{chat_id}] sending sticker12")
        await bot.send_sticker(chat_id, STICKER_12)

        await asyncio.sleep(2)
        logger.info(f"[{chat_id}] sending msg13")
        await bot.send_photo(chat_id, PHOTO_13, caption=MSG13_CAPTION, caption_entities=E(MSG13_ENT), reply_markup=kb_book())

        logger.info(f"[{chat_id}] DONE")

    except Exception as e:
        logger.error(f"[{chat_id}] ERROR in continue_after_scenario: {e}", exc_info=True)

# ─── handlers ────────────────────────────────────────────────────────────────

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(MSG1_TEXT, entities=E(MSG1_ENT), reply_markup=kb_start())

@dp.message(F.text == "что за история?")
async def handle_what(message: Message):
    await message.answer(MSG2_TEXT, entities=E(MSG2_ENT))
    await asyncio.sleep(2)
    await send_msg3_then_sticker4(message.chat.id)

@dp.message(F.text == "погнали!")
async def handle_go(message: Message):
    await send_msg3_then_sticker4(message.chat.id)

@dp.callback_query(F.data == "scenario_uzhas")
async def cb_uzhas(callback: CallbackQuery):
    await callback.answer("даа! это была реальная жуть!", show_alert=True)
    asyncio.ensure_future(continue_after_scenario(callback.message.chat.id, "uzhas"))

@dp.callback_query(F.data == "scenario_ugar")
async def cb_ugar(callback: CallbackQuery):
    await callback.answer("ха-ха! да, чел!", show_alert=True)
    asyncio.ensure_future(continue_after_scenario(callback.message.chat.id, "ugar"))

@dp.callback_query(F.data == "book_1")
async def cb_book1(callback: CallbackQuery):
    await callback.answer("да... тут кажется зажевалась печать...", show_alert=True)

@dp.callback_query(F.data == "book_2")
async def cb_book2(callback: CallbackQuery):
    await callback.answer("тут все ок!", show_alert=True)

@dp.callback_query(F.data == "book_3")
async def cb_book3(callback: CallbackQuery):
    await callback.answer("тут все нормально!", show_alert=True)

# ─── main ────────────────────────────────────────────────────────────────────

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
