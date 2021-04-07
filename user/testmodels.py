from models import insert, findby_email_and_password


def test_models_insert():
    insert('마이콜', 'michol@gmail.com', '1234', 'male')

def test_models_findby_email_and_password():
    result = findby_email_and_password('michol@gmail.com', '1234')
    print(result)

test_models_insert()
# test_models_findby_email_and_password()