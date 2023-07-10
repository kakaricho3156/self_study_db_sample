from db_config import Message


def update():
    user_name = input("変更する名前を入力してください")
    id = 1
    msg = Message.get_by_id(id)
    msg.user = user_name
    msg.save()


if __name__ == "__main__":
    update()
