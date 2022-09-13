import re

def check_reminder_regex(text:str):
    return re.match(r'^([0-9]{2}\.){2}[0-9]{4}\*\*.*',text)