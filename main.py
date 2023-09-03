import asyncio
from aiogram import Bot, Dispatcher
from config import CONFIG
from handlers import base, audio


bot = Bot(token=CONFIG.bot_token.get_secret_value())


async def main():
    dp = Dispatcher()

    dp.include_routers(base.router, audio.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

