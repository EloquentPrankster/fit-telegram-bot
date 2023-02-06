from db_api.get.get_access_db import get_access_db


def has_access(user: str) -> bool:
    """@user - message.from_user.username\n
        Returns True if user have access to command. False in another case
    """
    return user in get_access_db()
