from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor


def conn():
    return connect(
        user='webdb',
        password='webdb',
        host='localhost',
        port=3306,
        db='webdb',
        charset='utf8')



def findby_email_and_password(email, password):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = 'select no, name from user where email = %s and password = %s'
        cursor.execute(sql, (email, password))

        # 결과 받아오기
        result = cursor.fetchone() # 결과가 하나이기 때문에 fetchall 이 아니라 fetchone 으로 써야함

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return result

    except OperationalError as e:
        print(f'error: {e}')


def insert(name, email, password, gender):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'insert into user values(null, %s, %s, %s, %s, now())'
        count = cursor.execute(sql, (name, email, password, gender))  # %s로 바인딩 해주는것

        # commit
        # insert / update / delete 후에 꼭 commit 해줘야함!
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')


def findbyno(no):
    # sql = 'select name, email, gender from user where no = %s'
    # count execute(sql, )
    pass

def update(name, password):
    pass

# def deleteby_no_and_password(no, password):
#     try:
#         # 연결
#         db = conn()

#         # cursor 생성
#         cursor = db.cursor()

#         # SQL 실행
#         sql = 'delete from mysite_guestbook where no = %s and password = %s'
#         count = cursor.execute(sql, (no, password))

#         # commit
#         db.commit()

#         # 자원 정리
#         cursor.close()
#         db.close()

#         # 결과 반환
#         return count == 1

#     except OperationalError as e:
#         print(f'error: {e}')

