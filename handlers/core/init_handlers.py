def init_handlers():
    # start
    import handlers.start.start

    # cancel
    import handlers.cancel.cancel

    # shiman worktime
    import handlers.shiman_worktime.get_worktime
    import handlers.shiman_worktime.set_worktime

    # get group
    import handlers.group_list.get_full_group
    import handlers.group_list.get_subs

    # set group
    import handlers.group_list.set_full_group

    # queue
    import handlers.queue.set_queue
    import handlers.queue.get_queues

    # rights
    import handlers.rights.get_access
    import handlers.rights.set_access
    import handlers.rights.rem_access

    # reminder
    import handlers.reminder.get_reminder
    import handlers.reminder.set_reminder
    import handlers.reminder.rem_reminder

    # timetable
    import handlers.timetable.get_timetable
    import handlers.timetable.set_timetable

    # help
    import handlers.help.help

    # secret command
    import handlers.secret_command.secret_command

    # exclusion
    import handlers.exclusion.exclude
