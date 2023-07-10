from db_config import Message

if __name__ == "__main__":
    for msg in Message.select():
        print(msg.id, msg.user, msg.content, msg.pub_date)
