def auth_handler():

    key = input("Enter authentication code: ")
    # True - сохранить, False - не сохранять
    remember_device = True

    return key, remember_device
