from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import F, Router

from app.keyboard import *

router = Router()

@router.message(CommandStart())
async def start_of_aura(message: Message):
    await message.reply("Привет! Добро пожаловать. Чем я могу помочь?", reply_markup=keyboard1)

@router.message(F.text == "Geeks")
async def gre(message: Message):
    await message.reply(
        "Компания Geeks — это ведущий игрок на рынке IT-услуг и решений. Мы специализируемся на разработке программного обеспечения, внедрении IT-инфраструктуры и предоставлении консалтинговых услуг. Мы помогаем бизнесу достигать новых высот, обеспечивая качественные и современные решения.",
        reply_markup=geeks_keyboard
    )

@router.message(F.text == "Направления")
async def dir(message: Message):
    await message.reply("Вот наши основные направления работы. Выберите интересующее вас направление для получения дополнительной информации:", reply_markup=inline2)

@router.callback_query(F.data == "frontend")
async def frontend_info(callback: CallbackQuery):
    await callback.message.answer(
        "Фронтенд — это то, что мы видим на веб-страницах. Это создание визуального интерфейса и взаимодействие с пользователем. Фронтенд-разработчики работают над внешним видом сайтов и приложений, делая их удобными и привлекательными.",
        reply_markup=inline443
    )
    await callback.answer('Информация о фронтенде')

@router.callback_query(F.data == "dizain")
async def design_info(callback: CallbackQuery):
    await callback.message.answer(
        "Дизайн — это процесс создания визуального оформления продуктов. Хороший дизайн улучшает восприятие и функциональность, делая продукт не только красивым, но и удобным в использовании.",
        reply_markup=inline432
    )
    await callback.answer('Информация о дизайне')

@router.callback_query(F.data == "backend")
async def backend_info(callback: CallbackQuery):
    await callback.message.answer(
        "Бэкенд — это серверная часть приложений, которая отвечает за обработку данных и взаимодействие с клиентом. Бэкенд-разработчики занимаются созданием и поддержкой серверных систем и баз данных.",
        reply_markup=inline434
    )
    await callback.answer('Информация о бэкенде')

@router.callback_query(F.data == "android")
async def android_info(callback: CallbackQuery):
    await callback.message.answer(
        "Андроид — это операционная система для мобильных устройств от Google. Она обеспечивает гибкость и широкие возможности для пользователей и разработчиков приложений. Мы разрабатываем приложения, которые работают на этой платформе.",
        reply_markup=inline431
    )
    await callback.answer('Информация об Андроид')

@router.callback_query(F.data == "AIO")
async def aio_info(callback: CallbackQuery):
    await callback.message.answer(
        "AIO (All-In-One) — это концепция, включающая в себя комплексное решение, объединяющее различные инструменты и технологии. Например, это может быть интеграция Telegram-ботов с Python для автоматизации различных задач.",
    )
    await callback.answer('Информация о AIO')

@router.callback_query(F.data == "DJ")
async def django_info(callback: CallbackQuery):
    await callback.message.answer(
        "Django — это популярный веб-фреймворк для Python, который облегчает создание сложных и масштабируемых веб-приложений. Он предлагает множество встроенных инструментов для ускорения разработки.",
    )
    await callback.answer('Информация о Django')

@router.callback_query(F.data == "UI")
async def ui_info(callback: CallbackQuery):
    await callback.message.answer(
        "UI (User Interface) — это пользовательский интерфейс, который отвечает за взаимодействие пользователя с приложением. Хороший UI делает работу с приложением простой и интуитивно понятной.",
    )
    await callback.answer('Информация о UI')

@router.callback_query(F.data == "UX")
async def ux_info(callback: CallbackQuery):
    await callback.message.answer(
        "UX (User Experience) — это опыт взаимодействия пользователя с приложением. Это включает в себя удобство использования и удовлетворение потребностей пользователя. Хороший UX дизайн делает взаимодействие приятным и эффективным.",
    )
    await callback.answer('Информация о UX')

@router.callback_query(F.data == "web")
async def web_design_info(callback: CallbackQuery):
    await callback.message.answer(
        "Веб-дизайн включает в себя создание и оформление веб-страниц, чтобы они были привлекательными и удобными для пользователей. Это важный аспект разработки веб-сайтов и приложений.",
    )
    await callback.answer('Информация о веб-дизайне')

@router.callback_query(F.data == "WEB")
async def app_dev_info(callback: CallbackQuery):
    await callback.message.answer(
        "Разработка приложений охватывает создание программного обеспечения для различных платформ, включая веб, мобильные устройства и настольные компьютеры. Это включает в себя проектирование, кодирование и тестирование приложений.",
    )
    await callback.answer('Информация о разработке приложений')

@router.callback_query(F.data == "SEC")
async def security_info(callback: CallbackQuery):
    await callback.message.answer(
        "Безопасность приложений — это важный аспект разработки, включающий защиту данных и предотвращение несанкционированного доступа. Мы разрабатываем решения для обеспечения защиты ваших данных и систем.",
    )
    await callback.answer('Информация о безопасности')

@router.callback_query(F.data == "PO")
async def software_info(callback: CallbackQuery):
    await callback.message.answer(
        "Программное обеспечение (ПО) — это набор программ и систем, которые обеспечивают функциональность и управление устройствами. Мы занимаемся разработкой ПО, адаптированного под ваши нужды.",
    )
    await callback.answer('Информация о ПО')

@router.callback_query(F.data == "pyt")
async def python_info(callback: CallbackQuery):
    await callback.message.answer(
        "Python — это один из самых популярных языков программирования благодаря своей простоте и мощным возможностям. Он широко используется для веб-разработки, анализа данных, искусственного интеллекта и многого другого.",
    )
    await callback.answer('Информация о Python')

@router.callback_query(F.data == "HTML")
async def html_info(callback: CallbackQuery):
    await callback.message.answer(
        "HTML (HyperText Markup Language) — это основной язык разметки для создания веб-страниц. Он описывает структуру страницы с помощью различных элементов и тегов.",
    )
    await callback.answer('Информация о HTML')

@router.callback_query(F.data == "CSS")
async def css_info(callback: CallbackQuery):
    await callback.message.answer(
        "CSS (Cascading Style Sheets) — это язык стилей, который используется для оформления веб-страниц. Он позволяет задавать внешний вид элементов HTML, такие как цвета, шрифты и макеты.",
    )
    await callback.answer('Информация о CSS')

@router.callback_query(F.data == "JS")
async def js_info(callback: CallbackQuery):
    await callback.message.answer(
        "JavaScript (JS) — это язык программирования, используемый для создания динамических и интерактивных элементов на веб-страницах. Он позволяет делать веб-страницы более функциональными и отзывчивыми.",
    )
    await callback.answer('Информация о JavaScript')
