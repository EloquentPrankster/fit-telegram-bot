from bot import disp
from aiogram import types


@disp.message_handler(commands=['cancel'], state='*')
async def cancel(message: types.Message):
    state = disp.current_state(chat=message.chat.id, user=message.from_user.id)
    if await state.get_state() is not None:
        await state.set_state(state=None)
        await message.answer('Действие отменено')
