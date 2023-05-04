from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
back = {
    "uzl": "Ortga⬅️",
    "uzk": "Ортга⬅️",
    "ru": "Назад⬅️",
    "en": "Go back⬅️️"
}

main_menu = {
    'uzl': "Asosiy menu",
    'uzk': "Асосий меню",
    'ru': "Главное меню",
    'en': "Main menu"
}
another = {
    "uzl": f"Boshqa manzil!",
    "uzk": f"Бошқа манзил!",
    "ru": f"Другой манзил!",
    "en": f"Another manzil!"
}

def kb_endOfManzil(lang):
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb.insert(InlineKeyboardButton(text=another[lang], callback_data="calling-manzil"))
    ikb.insert(InlineKeyboardButton(text=back[lang], callback_data="back-manzil"))
    ikb.insert(InlineKeyboardButton(text=main_menu[lang], callback_data="main-menu"))
    return ikb


def kb_manzil_option_to_continue(rem_ayahs, lang):
    next_ayahs = {
        "uzl": f"Keyingi {rem_ayahs} ta oyat➡️",
        "uzk": f"Кейинги {rem_ayahs} та оят➡️",
        "ru": f"Cледушие {rem_ayahs} аяти➡️",
        "en": f"Next {rem_ayahs} ayahs➡️"
    }
    ikb= InlineKeyboardMarkup(row_width=2)
    ikb.insert(InlineKeyboardButton(text=next_ayahs[lang], callback_data="next-ayahs-manzil"))
    ikb.insert(InlineKeyboardButton(text=another[lang], callback_data="calling-manzil"))
    ikb.insert(InlineKeyboardButton(text=back[lang], callback_data="back-manzil"))
    ikb.insert(InlineKeyboardButton(text=main_menu[lang], callback_data="main-menu"))
    return ikb