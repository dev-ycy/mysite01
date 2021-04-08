from django.shortcuts import render, redirect
from . import models

def joinform(request):
    return render(request, 'user/joinform.html')


def join(request):
    # 파라미터 받기
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']

    # DB 적용
    models.insert(name, email, password, gender)

    # 응답
    return redirect('/user/joinsuccess')


def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')


def loginform(request):
    return render(request, 'user/loginform.html')


def login(request):
    email = request.POST['email']
    password = request.POST['password']

    result = models.findby_email_and_password(email, password)
    # print(result)
    if result is None:
        return redirect('/user/loginform?result=fail')

    # 로그인 처리
    request.session["authuser"] = result    # result 는 dict 형태
    # authuser 대신 다른거 써도 무방

    return redirect('/')


def logout(request):
    del request.session['authuser']
    return redirect('/')


def updateform(request):
    # Access Control (접근 제어) - url 직접접근 막음
    authuser = request.session.get("authuser")
    # "authuser"에 해당되는 객체가 없으면 None을 반환
    if authuser is None:
        return redirect('/')
    # authuser = request.session['authuser']
    no = str(authuser['no'])
    result = models.findbyno(no)
    # print(result) # {'name': '둘리', 'email': 'kickscar@gmail.com', 'gender': 'male'}
    data = {
        "user": result
    }
    return render(request, 'user/updateform.html', data)


def update(request):
    no = request.POST["no"]
    name = request.POST["name"]
    gender = request.POST["gender"]

    if request.POST["password"]:
        password = request.POST["password"]
    else:    
        password = models.findpw_byno(no)["password"] 
    print(name, password, gender, no)
    models.update(name, password, gender, no)

    # session name 변경
    request.session['authuser']['name'] = name
    # 위 방법은 session 변경 안됨(session storage에 저장안됨)
    # 위 방법으로 가능하게 하려면, 옵션 변경하면 됨.
    # settings.py에서 SESSION_SAVE_EVERY_REQUEST = True
    # request.session['authuser'] = {
    #     'no': no,
    #     'name': name
    # }

    return redirect('/')



