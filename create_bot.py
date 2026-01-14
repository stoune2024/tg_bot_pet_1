import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from asyncpg_lite import DatabaseManager
from config import settings

# получаем список администраторов из .env
admins = [int(admin_id) for admin_id in settings.ADMINS.split(",")]

# настраиваем логирование и выводим в переменную для отдельного использования в нужных местах
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# инициируем объект, который будет отвечать за взаимодействие с базой данных
db_manager = DatabaseManager(
    db_url=settings.POSTGRES_URL, deletion_password=settings.ROOT_PASS
)

# инициируем объект бота, передавая ему parse_mode=ParseMode.HTML по умолчанию
bot = Bot(
    token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

# инициируем объект бота
dp = Dispatcher()
