import asyncio
import aioschedule as shed
from sheduler.task_definition import task_definition


async def sheduler():
    task_definition()
    while True:
        await shed.run_pending()
        await asyncio.sleep(1)
