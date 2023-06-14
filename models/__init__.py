from peewee import *
from config import DATABASE_NAME
from playhouse.db_url import connect

db = connect(DATABASE_NAME) 

class BaseModel(Model):
    class Meta:
        database = db


class Student(BaseModel):
    id = AutoField()
    surname = TextField(null=False)
    name = TextField(null=False,)
    patronymic = TextField(null=False)
    subgroup = SmallIntegerField(null=False)
    position = IntegerField(null=True)
    position_in_subgroup = IntegerField(null=True)


class Description(BaseModel):
    id = AutoField()
    description = TextField(null=False)


class Username(BaseModel):
    id = AutoField()
    username = TextField(null=False, unique=True)


MODELS = [Student,  Description, Username]
