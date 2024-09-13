from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)

buttons1 = [
    [KeyboardButton(text="Geeks"), KeyboardButton(text="Направления")]
]
keyboard1 = ReplyKeyboardMarkup(keyboard=buttons1, resize_keyboard=True)

inline1 = [
    [InlineKeyboardButton(text="Бэкенд", callback_data='backend')],
    [InlineKeyboardButton(text="Фронтенд", callback_data='frontend')],
    [InlineKeyboardButton(text="UX/UI Дизайн", callback_data='dizain')],
    [InlineKeyboardButton(text="Андроид", callback_data='android')]
]
inline2 = InlineKeyboardMarkup(inline_keyboard=inline1)

geeks_inline = [
    [InlineKeyboardButton(text="О Geeks.pro", url="https://geeks.kg/geeks-pro")],
    [InlineKeyboardButton(text="О Geeks студио", url="https://geekstudio.kg/")],
    [InlineKeyboardButton(text="Главный сайт Geeks", url="https://geeks.kg/")]
]
geeks_keyboard = InlineKeyboardMarkup(inline_keyboard=geeks_inline)

backend_inline = [
    [InlineKeyboardButton(text="Django", callback_data='DJ')],
    [InlineKeyboardButton(text="Python", callback_data='pyt')],
    [InlineKeyboardButton(text="Aiogram", callback_data='AIO')],
]
inline434 = InlineKeyboardMarkup(inline_keyboard=backend_inline)

frontend_inline = [
    [InlineKeyboardButton(text="HTML", callback_data='HTML')],
    [InlineKeyboardButton(text="JavaScript (JS)", callback_data='JS')],
    [InlineKeyboardButton(text="CSS", callback_data='CSS')],
]
inline443 = InlineKeyboardMarkup(inline_keyboard=frontend_inline)

android_inline = [
    [InlineKeyboardButton(text="Разработка приложений", callback_data='WEB')],
    [InlineKeyboardButton(text="Безопасность", callback_data='SEC')],
    [InlineKeyboardButton(text="Программное обеспечение", callback_data='PO')],
]
inline431 = InlineKeyboardMarkup(inline_keyboard=android_inline)

dizain_inline = [
    [InlineKeyboardButton(text="UI Дизайн", callback_data='UI')],
    [InlineKeyboardButton(text="UX Дизайн", callback_data='UX')],
    [InlineKeyboardButton(text="Веб-дизайн", callback_data='web')],
]
inline432 = InlineKeyboardMarkup(inline_keyboard=dizain_inline)
