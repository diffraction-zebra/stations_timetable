import asyncio
import sys

import logging

from telegram import bot, dispatcher


async def main():
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
