import logging
from aiogram import types
from aiogram.dispatcher import FSMContext


async def cancel(message: types.Message, state: FSMContext):
    if await state.get_state() is not None:
        await state.finish()
        await message.answer('Действие отменено')
    logging.info(f"cancel completed")