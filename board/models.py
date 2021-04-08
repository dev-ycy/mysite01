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


# def findall():
#     try:
#         # 연결
#         db = conn()

#         # cursor 생성
#         cursor = db.cursor(DictCursor)

#         # SQL 실행
#         sql = '''
#         select no, name, message, date_format(reg_date, "%Y-%m-%d %p %h:%i:%s") as reg_date
#         from mysite_guestbook
#         order by reg_date desc'''
#         cursor.execute(sql)

#         # 결과 받아오기
#         results = cursor.fetchall()

#         # 자원 정리
#         cursor.close()
#         db.close()

#         # 결과 반환
#         return results

#     except OperationalError as e:
#         print(f'error: {e}')


def findall():
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = '''
        select board.no, board.title, board.contents, board.hit,
                date_format(board.reg_date, "%Y-%m-%d %H:%i") as reg_date,
                board.g_no, board.o_no, board.depth, board.user_no, user.name
        from board
        left outer join user
        on board.user_no = user.no
        order by reg_date desc
        '''
        # 아래는 join 없는버전
        # sql = ''' 
        # select no, title, contents, hit, date_format(reg_date, "%Y-%m-%d %p %h:%i:%s") as reg_date,
        # g_no, o_no, depth, user_no
        # from board
        # order by reg_date desc
        # '''
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


# def findbyno(no):
#     # sql = 'select name, email, gender from user where no = %s'
#     # count execute(sql, )
#     pass
#
def findby_no(no):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = '''
        select no, title, contents, hit,
                date_format(reg_date, "%%Y-%%m-%%d %%H:%%i") as reg_date,
                g_no, o_no, depth, user_no
        from board
        where no = %s
        '''
        cursor.execute(sql, (no,))

        # 결과 받아오기
        result = cursor.fetchone()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return result

    except OperationalError as e:
        print(f'error: {e}')


def insert(title, contents, hit, g_no, o_no, depth, user_no):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'insert into board values(null, %s, %s, %s, now(), %s, %s, %s, %s);'
        count = cursor.execute(sql, (title, contents, hit, g_no, o_no, depth, user_no))  

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


def deleteby_no(no):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'delete from board where no = %s'
        count = cursor.execute(sql, (no))

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')

