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
    if authuser is None:
        return redirect('/')
    # authuser = request.session['authuser']
    result = models.findbyno(authuser['no'])
    return render(request, 'user/updateform.html', result)


def update(request):
    pass


