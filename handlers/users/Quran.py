from loader import dp, bot, db_users
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.options_for_Quran import options_to_read
from keyboards.inline.kb_for_juzs import getting_list_of_juzs
from keyboards.inline.kb_for_surahs import getting_list_of_surahs
from states.states_for_Quran import states_for_Quran
from states.language_state import Language

from keyboards.inline.kb_for_Quran import going_back_to_Quran_options

delete = bool


@dp.message_handler(state=Language.Choosing_book)
async def quran_cmd(message: types.Message, state: FSMContext):

    text = {
        'uzl': "Qur'onni uch xil uslubda o'qishingiz mumkin. Ikkalasidan birini tanglang!",
        'uzk': "Қуръонни уч хил услубда ўқишингиз мумкин. Иккаласидан бирини тангланг!",
        'ru': "Вы можете читать Коран тремя способами. Пожалуйста, выберите один из трех!",
        'en': "You can read Quran in three ways. Please choose one!"
    }
    lang = db_users.get_user_language(id=message.chat.id)[0]
    await message.answer(text[lang], reply_markup=await options_to_read(lang, message))
    await states_for_Quran.option.set()



@dp.message_handler(state=states_for_Quran.option)
async def option_to_read_cmd(message: types.Message, state: FSMContext):
    global delete


    lang = db_users.get_user_language(id=message.chat.id)[0]

    async with state.proxy() as data:
        data['latest-ayah'] = 1
        data['latest-ayah-juz'] = 1


    text = message.text
    Juz = {
        'uzl': "Juzlar",
        'uzk': "Жузлар",
        'ru': "Жузи",
        'en': "Juzs"
    }
    Surah = {
        'uzl': "Suralar",
        'uzk': "Суралар",
        'ru': "Суры",
        'en': "Surahs"
    }
    Page = {
        'uzl': "Varaqlar",
        'uzk': "Варақлар",
        'ru': "Страницы",
        'en': "Pages"
    }
    manzil = {
        'uzl': "Manzillar",
        'uzk': "Манзилы",
        'ru': "Манзилы",
        'en': "Manzils"
    }
    if text in Juz[lang]:
        kb = await getting_list_of_juzs(lang)
        kb.insert(await going_back_to_Quran_options(lang))
        text = {
            'uzl': "Juz raqamini kiriting! Yoki pastdagi tugmani bosing!",
            'uzk': "Жуз рақамини киритинг! Ёки пастдаги тугмани босинг!",
            'ru': "Введите номер жуза! Или нажмите кнопку ниже!",
            'en': "Enter juz number. Or click the button below"
        }
        await message.answer(text=text[lang], reply_markup=await getting_list_of_juzs(lang))
        await states_for_Quran.juz.set()
    elif text in Surah[lang]:

        text = {
            'uzl': "Sura raqamini kiriting! Yoki pastdagi tugmani bosing!",
            'uzk': "Сура рақамини киритинг! Ёки пастдаги тугмани босинг!",
            'ru': "Введите номер cура! Или нажмите кнопку ниже!",
            'en': "Enter surah number. Or click the button below"
        }
        await message.answer(text=text[lang], reply_markup=await getting_list_of_surahs(lang))
        await states_for_Quran.surah.set()

    elif text in Page[lang]:
        text = {
            'uzl': "Varaq raqamini kiriting!",
            'uzk': "Варақ рақамини киритинг!",
            'ru': "Введите номер страницы!",
            'en': "Enter the page number"
        }
        await message.answer(text=text[lang])
        await states_for_Quran.page.set()
    elif text in manzil[lang]:
        text = {
            'uzl': "Manzil raqamini kiriting!",
            'uzk': "Манзил рақамини киритинг!",
            'ru': "Введите номер манзила!",
            'en': "Enter the manzil number"
        }
        await message.answer(text=text[lang])
        await state.set_state('manzil')

