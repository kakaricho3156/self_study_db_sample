from db_config import Message


def delete():
    id = 2
    msg = Message.get_by_id(id)
    msg.delete_instance()


if __name__ == "__main__":
    delete()
