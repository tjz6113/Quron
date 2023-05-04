from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

next_page = {
    "uzl": "Keyingi varaq",
    "uzk": "Кейинги варақ",
    "ru": "Следущая страница",
    "en": "Next page"
}
back = {
    "uzl": "Ortga⬅️",
    "uzk": "Ортга⬅️",
    "ru": "Назад⬅️",
    "en": "Go back⬅️️"
}
main_menu = {
    "uzl": "Asosiy menu",
    "uzk": "Асосий меню",
    "ru": "Главное меню",
    "en": "Main menu"
}


def end_page(lang):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.insert(InlineKeyboardButton(text=next_page[lang], callback_data="next-page"))
    kb.insert(InlineKeyboardButton(text=back[lang] + "⬅️", callback_data="go-back"))
    kb.insert(InlineKeyboardButton(text=main_menu[lang] + "🏠", callback_data="main-menu"))
    return kb
