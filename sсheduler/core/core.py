import asyncio
import aioschedule as sched
from ..scheduled_tasks import scheduled_tasks


async def scheduler():
    scheduled_tasks()
    while True:
        await sched.run_pending()
        await asyncio.sleep(1)
