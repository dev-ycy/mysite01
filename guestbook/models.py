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


def findall():
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = '''
        select no, name, message, date_format(reg_date, "%Y-%m-%d %p %h:%i:%s") as reg_date
        from mysite_guestbook
        order by reg_date desc'''
        cursor.execute(sql)

        # 결과 받아오기
        results = cursor.fetchall()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return results

    except OperationalError as e:
        print(f'error: {e}')


def insert(name, password, message):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'insert into mysite_guestbook values(null, %s, %s, %s, now())'
        count = cursor.execute(sql, (name, password, message))  # %s로 바인딩 해주는것

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


def deleteby_no_and_password(no, password):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'delete from mysite_guestbook where no = %s and password = %s'
        count = cursor.execute(sql, (no, password))

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')

