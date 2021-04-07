from models import findall, insert


def test_models_insert():
    insert('안녕하세요오오오', '안녕하세요?', '0', '1', '1', '0', '2')


# def test_models_findby_email_and_password():
#     result = findby_email_and_password('michol@gmail.com', '1234')
#     print(result)


def test_model_findall():
    results = findall()
    print(results)


test_models_insert()  # OK!
# test_model_findall()   # OK!



