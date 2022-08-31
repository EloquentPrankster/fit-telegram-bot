def init_handlers():
    # start
    import handlers.start.start
    # shiman worktime
    import handlers.shiman_worktime.get_worktime
    import handlers.shiman_worktime.set_worktime
    # get group
    import handlers.group_list.get_full_group
    import handlers.group_list.get_sub_1
    import handlers.group_list.get_sub_2
    # set group
    import handlers.group_list.set_full_group
    # vk
    import handlers.getmessagefromvk
