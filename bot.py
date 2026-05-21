import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton,
    ReplyKeyboardRemove
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

# Фото для сообщения 8 — берём наибольшее разрешение (индекс 3)
PHOTO_8_UZHAS = "AgACAgIAAxkBAAFKNNdqDlZS7bcPu8XCnmO85bs3aCx3SAACTyFrG1iucEitsGLlN_gUBwEAAwIAA3kAAzsE"
PHOTO_8_UGAR  = "AgACAgIAAxkBAAFKNOVqDldfhxuz1QGrrnb0i9gDpG7JxwACUCFrG1iucEigCDk-Bb0nxwEAAwIAA3kAAzsE"

# Сообщение 10 — signal.png (фото из Telegram, наибольшее)
PHOTO_10 = "AgACAgIAAxkBAAFKNOdqDlefOiJPnYc08f049HOW9uQNVAACZiFrG1iucEjMIJu3x49ljQEAAwIAA3kAAzsE"

# Сообщение 11 — boys.png
PHOTO_11 = "AgACAgIAAxkBAAFKNOtqDlfA9YPPHKRRMuXLhTZO_IpWvQACbCFrG1iucEiIyitDkLv0DwEAAwIAA3kAAzsE"

# Сообщение 13 — book.png
PHOTO_13 = "AgACAgIAAxkBAAFKNPJqDlggLlebgI5oe5fFoib_FJiGiQACbiFrG1iucEh9a7stKUMEeAEAAwIAA3kAAzsE"

# ─── helpers для custom_emoji entities ───────────────────────────────────────

def make_entities(text: str, spec: list) -> list:
    """
    spec = список dict: {"offset": int, "length": 2, "type": "custom_emoji"/"blockquote", "custom_emoji_id": str}
    Возвращает список MessageEntity-совместимых dict для send_message(entities=...)
    """
    from aiogram.types import MessageEntity
    result = []
    for s in spec:
        kwargs = {"type": s["type"], "offset": s["offset"], "length": s["length"]}
        if s["type"] == "custom_emoji":
            kwargs["custom_emoji_id"] = s["custom_emoji_id"]
        result.append(MessageEntity(**kwargs))
    return result

# ─── тексты и entities ───────────────────────────────────────────────────────

# Сообщение 1
MSG1_TEXT = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD фух! ну и история, бро!\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "об этом надо написать книгу!"
)
MSG1_ENTITIES = [
    {"offset": 0,  "length": 44, "type": "blockquote"},
    {"offset": 0,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220121337665726730"},
    {"offset": 2,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220025809003130352"},
    {"offset": 4,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219901499764678745"},
    {"offset": 7,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5221978279661049220"},
    {"offset": 9,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219803776373790987"},
    {"offset": 11, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219780991572286175"},
    {"offset": 38, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5222411637566247305"},
    {"offset": 40, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219960315046830005"},
    {"offset": 42, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219951742292109016"},
    {"offset": 45, "length": 28, "type": "blockquote"},
]

# Сообщение 2
MSG2_TEXT = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD эээ? давай без вопросов...\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "берись за ручку!"
)
MSG2_ENTITIES = [
    {"offset": 0,  "length": 47, "type": "blockquote"},
    {"offset": 0,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220138654973862915"},
    {"offset": 2,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220203766678068592"},
    {"offset": 4,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220091818355499138"},
    {"offset": 7,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220069613374579574"},
    {"offset": 9,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219958725908930395"},
    {"offset": 11, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219898776755412740"},
    {"offset": 41, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220028501947623425"},
    {"offset": 43, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220131825975862523"},
    {"offset": 45, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220061650505214423"},
    {"offset": 48, "length": 16, "type": "blockquote"},
]

# Сообщение 3
MSG3_TEXT = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD я задам темп, а ты продолжай\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "это был обычный летний день..."
)
MSG3_ENTITIES = [
    {"offset": 0,  "length": 49, "type": "blockquote"},
    {"offset": 0,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220121337665726730"},
    {"offset": 2,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220025809003130352"},
    {"offset": 4,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219901499764678745"},
    {"offset": 7,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5221978279661049220"},
    {"offset": 9,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219803776373790987"},
    {"offset": 11, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219780991572286175"},
    {"offset": 43, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5222411637566247305"},
    {"offset": 45, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219960315046830005"},
    {"offset": 47, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219951742292109016"},
    {"offset": 50, "length": 30, "type": "blockquote"},
]

# Сообщение 5
MSG5_TEXT = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD чувак, да мы как братья грим!\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "но в гриме только я, да и не братья… не суть, бро! пока не разогнались, давай-ка я наберу знакомому дизайнеру - пусть глянет на наши труды"
)
MSG5_ENTITIES = [
    {"offset": 0,  "length": 50, "type": "blockquote"},
    {"offset": 0,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220138654973862915"},
    {"offset": 2,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220203766678068592"},
    {"offset": 4,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220091818355499138"},
    {"offset": 7,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220069613374579574"},
    {"offset": 9,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219958725908930395"},
    {"offset": 11, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219898776755412740"},
    {"offset": 44, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220028501947623425"},
    {"offset": 46, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220131825975862523"},
    {"offset": 48, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220061650505214423"},
    {"offset": 51, "length": 138,"type": "blockquote"},
]

# Сообщение 7
MSG7_TEXT = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DDпривет! что тут у вас? \n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD братаан! ты офигеешь!\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD"
)
MSG7_ENTITIES = [
    {"offset": 0,  "length": 43, "type": "blockquote"},
    {"offset": 0,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220138654973862915"},
    {"offset": 2,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220203766678068592"},
    {"offset": 4,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220091818355499138"},
    {"offset": 7,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219785995209185967"},
    {"offset": 9,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219935490135860144"},
    {"offset": 11, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219909690267312927"},
    {"offset": 37, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219944539631949923"},
    {"offset": 39, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219750793657226454"},
    {"offset": 41, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5222207540720343242"},
    {"offset": 44, "length": 42, "type": "blockquote"},
    {"offset": 44, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220138654973862915"},
    {"offset": 46, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220203766678068592"},
    {"offset": 48, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220091818355499138"},
    {"offset": 51, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219944539631949923"},
    {"offset": 53, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219750793657226454"},
    {"offset": 55, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5222207540720343242"},
    {"offset": 72, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220138654973862915"},
    {"offset": 74, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220203766678068592"},
    {"offset": 76, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220091818355499138"},
]

# Caption для сообщений 8 (одинаковый для обоих сценариев)
MSG8_CAPTION = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DDйоу… как бы помягче…\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "давай прикинем, как будет выглядеть текст, отдельные элементы и прочее…"
)
MSG8_ENTITIES = [
    {"offset": 0,  "length": 40, "type": "blockquote"},
    {"offset": 0,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220138654973862915"},
    {"offset": 2,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220203766678068592"},
    {"offset": 4,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220091818355499138"},
    {"offset": 7,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219785995209185967"},
    {"offset": 9,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219935490135860144"},
    {"offset": 11, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219909690267312927"},
    {"offset": 33, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219944539631949923"},
    {"offset": 35, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219750793657226454"},
    {"offset": 37, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5222207540720343242"},
    {"offset": 41, "length": 74, "type": "blockquote"},
]

# Сообщение 9 — просто текст
MSG9_TEXT = "(далее — посты в хронологическом порядке, которые дропнутся разом. без интерактива. сорри.)"

# Caption сообщения 10 (signal.png)
MSG10_CAPTION = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD стэнд ап!\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "сигнал отпечатали!"
)
MSG10_ENTITIES = [
    {"offset": 0,  "length": 30, "type": "blockquote"},
    {"offset": 0,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220121337665726730"},
    {"offset": 2,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220025809003130352"},
    {"offset": 4,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219901499764678745"},
    {"offset": 7,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5221978279661049220"},
    {"offset": 9,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219803776373790987"},
    {"offset": 11, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219780991572286175"},
    {"offset": 24, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5222411637566247305"},
    {"offset": 26, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219960315046830005"},
    {"offset": 28, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219951742292109016"},
    {"offset": 31, "length": 20, "type": "blockquote"},
]

# Caption сообщения 11 (boys.png)
MSG11_CAPTION = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD заходи справа!\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "у него отцентрованное зрение!"
)
MSG11_ENTITIES = [
    {"offset": 0,  "length": 35, "type": "blockquote"},
    {"offset": 0,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220121337665726730"},
    {"offset": 2,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220025809003130352"},
    {"offset": 4,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219901499764678745"},
    {"offset": 7,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5221978279661049220"},
    {"offset": 9,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219803776373790987"},
    {"offset": 11, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219780991572286175"},
    {"offset": 28, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5222411637566247305"},
    {"offset": 30, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219960315046830005"},
    {"offset": 32, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219951742292109016"},
    {"offset": 36, "length": 29, "type": "blockquote"},
]

# Caption сообщения 13 (book.png)
MSG13_CAPTION = (
    "\U0001F5DD\U0001F5DD\U0001F5DD\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD дай правки типографии\n"
    "\U0001F5DD\U0001F5DD\U0001F5DD"
)
MSG13_ENTITIES = [
    {"offset": 0,  "length": 42, "type": "blockquote"},
    {"offset": 0,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220121337665726730"},
    {"offset": 2,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5220025809003130352"},
    {"offset": 4,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219901499764678745"},
    {"offset": 7,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5221978279661049220"},
    {"offset": 9,  "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219803776373790987"},
    {"offset": 11, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219780991572286175"},
    {"offset": 27, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5222411637566247305"},
    {"offset": 29, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219960315046830005"},
    {"offset": 31, "length": 2,  "type": "custom_emoji", "custom_emoji_id": "5219951742292109016"},
]

# ─── keyboards ───────────────────────────────────────────────────────────────

def kb_start() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="что за история?"), KeyboardButton(text="погнали!")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

def kb_scenario() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="этот ужас...", callback_data="scenario_uzhas")
    builder.button(text="такой угар!", callback_data="scenario_ugar")
    builder.adjust(2)
    return builder.as_markup()

def kb_book() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="1", callback_data="book_1")
    builder.button(text="2", callback_data="book_2")
    builder.button(text="3", callback_data="book_3")
    builder.adjust(3)
    return builder.as_markup()

# ─── helpers ─────────────────────────────────────────────────────────────────

def build_entities(spec: list):
    from aiogram.types import MessageEntity
    result = []
    for s in spec:
        kwargs = {"type": s["type"], "offset": s["offset"], "length": s["length"]}
        if s.get("custom_emoji_id"):
            kwargs["custom_emoji_id"] = s["custom_emoji_id"]
        result.append(MessageEntity(**kwargs))
    return result

async def send_msg3_and_after(chat_id: int, scenario: str | None = None):
    """Отправляет сообщение 3, потом 4 (стикер) через 3 сек."""
    await bot.send_message(
        chat_id,
        MSG3_TEXT,
        entities=build_entities(MSG3_ENTITIES),
        reply_markup=ReplyKeyboardRemove(),
    )
    await asyncio.sleep(3)
    # Сообщение 4 — стикер с inline-кнопками
    await bot.send_sticker(
        chat_id,
        STICKER_4,
        reply_markup=kb_scenario(),
    )

async def continue_after_scenario(chat_id: int, chosen: str):
    """
    Шаги 3-11 после выбора сценария:
    5 сек → msg5, 2 сек → sticker6, 3 сек → msg7,
    → msg8 (фото по сценарию),
    10 сек → msg9, 2 сек → msg10(фото signal),
    5 сек → msg11(фото boys), 5 сек → sticker12,
    2 сек → msg13(фото book + кнопки).
    """
    await asyncio.sleep(5)
    # Msg 5
    await bot.send_message(chat_id, MSG5_TEXT, entities=build_entities(MSG5_ENTITIES))

    await asyncio.sleep(2)
    # Msg 6 — стикер
    await bot.send_sticker(chat_id, STICKER_6)

    await asyncio.sleep(3)
    # Msg 7
    await bot.send_message(chat_id, MSG7_TEXT, entities=build_entities(MSG7_ENTITIES))

    # Msg 8 — фото по сценарию
    photo_id = PHOTO_8_UZHAS if chosen == "uzhas" else PHOTO_8_UGAR
    await bot.send_photo(
        chat_id,
        photo_id,
        caption=MSG8_CAPTION,
        caption_entities=build_entities(MSG8_ENTITIES),
    )

    await asyncio.sleep(10)
    # Msg 9
    await bot.send_message(chat_id, MSG9_TEXT)

    await asyncio.sleep(2)
    # Msg 10 — signal.png
    await bot.send_photo(
        chat_id,
        PHOTO_10,
        caption=MSG10_CAPTION,
        caption_entities=build_entities(MSG10_ENTITIES),
    )

    await asyncio.sleep(5)
    # Msg 11 — boys.png
    await bot.send_photo(
        chat_id,
        PHOTO_11,
        caption=MSG11_CAPTION,
        caption_entities=build_entities(MSG11_ENTITIES),
    )

    await asyncio.sleep(5)
    # Msg 12 — стикер
    await bot.send_sticker(chat_id, STICKER_12)

    await asyncio.sleep(2)
    # Msg 13 — book.png + кнопки
    await bot.send_photo(
        chat_id,
        PHOTO_13,
        caption=MSG13_CAPTION,
        caption_entities=build_entities(MSG13_ENTITIES),
        reply_markup=kb_book(),
    )

# ─── handlers ────────────────────────────────────────────────────────────────

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        MSG1_TEXT,
        entities=build_entities(MSG1_ENTITIES),
        reply_markup=kb_start(),
    )

@dp.message(F.text == "что за история?")
async def handle_what(message: Message):
    # Msg 2
    await message.answer(MSG2_TEXT, entities=build_entities(MSG2_ENTITIES))
    await asyncio.sleep(2)
    # Msg 3 + дальше
    await send_msg3_and_after(message.chat.id)

@dp.message(F.text == "погнали!")
async def handle_go(message: Message):
    # Сразу msg 3 + дальше
    await send_msg3_and_after(message.chat.id)

@dp.callback_query(F.data == "scenario_uzhas")
async def cb_uzhas(callback: CallbackQuery):
    await callback.answer("даа! это была реальная жуть!", show_alert=True)
    asyncio.create_task(continue_after_scenario(callback.message.chat.id, "uzhas"))

@dp.callback_query(F.data == "scenario_ugar")
async def cb_ugar(callback: CallbackQuery):
    await callback.answer("ха-ха! да, чел!", show_alert=True)
    asyncio.create_task(continue_after_scenario(callback.message.chat.id, "ugar"))

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
