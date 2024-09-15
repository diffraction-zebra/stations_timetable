import os
import itertools

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from timetable import get_departure_time


router = Router()


stations = eval(os.getenv('stations'))

builder = ReplyKeyboardBuilder()
for comb in itertools.combinations(stations.keys(), 2):
    left_to_right = f"{comb[0]} -> {comb[1]}"
    right_to_left = f"{comb[1]} -> {comb[0]}"
    builder.button(text=left_to_right)
    builder.button(text=right_to_left)


async def default_answer(message):
    await message.answer("Choose direction", reply_markup=builder.as_markup())


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    await default_answer(message)


@router.message()
async def command_start(message: Message) -> None:
    try:
        left, right = message.text.split(' -> ')
        times = get_departure_time(stations[left],
                                   stations[right])
        await message.answer('\n'.join(times))
    except Exception as e:
        print(f'exception {e} occur')
        await default_answer(message)
