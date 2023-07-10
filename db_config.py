import os
import datetime
import logging
from playhouse.db_url import connect
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField

load_dotenv()

logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# db = SqliteDatabase("peewee_db.sqlite")
db = connect(os.environ.get("DATABASE"))
# db = connect(os.environ.get("DATABASE") or "sqlite:///peewee_db.sqlite")

if not db.connect():
    print("接続NG")
    exit()


class Message(Model):
    id = IntegerField(primary_key=True)
    user = CharField()
    content = TextField
    pub_date = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = db
        table_name = "message"


db.create_tables([Message])
