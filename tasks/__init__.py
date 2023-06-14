import asyncio
from datetime import datetime
import logging
from uu import Error
from tasks.tasks import list_of_tasks


class TaskManager:
    def create_task_schedule(self, func, target_time: int, bot, db_manager=None):
        async def task_schedule():
            if isinstance(target_time, int):
                while True:
                    # start at xx:xx:00
                    current_time_seconds = datetime.now().second
                    logging.info(f"Timedelta module: {(60 - current_time_seconds) % target_time}")
                    logging.info(f"Timedelta: {60 - current_time_seconds}")
                    await asyncio.sleep(
                        (60 - current_time_seconds) % target_time
                        if current_time_seconds % target_time != 0
                        else target_time)
                    await func(bot, db_manager)
            else:
                raise Error("Wrong type of target_time")
        return task_schedule

    def schedule(self, bot, db_manager):
        if len(list_of_tasks) == 0:
            return logging.info("No tasks to schedule")
        for i in list_of_tasks:
            task_schedule = self.create_task_schedule(
                i['func'], target_time=i['time'], bot=bot, db_manager=db_manager)
            asyncio.create_task(task_schedule())
        return logging.info("Tasks scheduled")
