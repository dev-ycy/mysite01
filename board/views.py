from django.shortcuts import render, redirect
from . import models


def index(request):
    results = models.findall()
    data = {"board_list": results}
    # print(data)
    return render(request, 'board/index.html', data)
    

def view(request):
    no = request.GET["no"]
    print(no)
    result = models.findby_no(no)
    print(result)

    # hit(조회수 +1 해야함) -- 반영이안됨...SQL코드 수정해야함
    # print(result["hit"])
    # result["hit"] = result["hit"] + 1
    # print(result["hit"])
    data = {"board": result}
    data['board']['user_no'] = str(data['board']['user_no'])

    return render(request, 'board/view.html', data)


def writeform(request):
    return render(request, 'board/writeform.html')

def write(request):
    title = request.POST["title"]
    contents = request.POST["contents"]
    print(request.session)
    authuser = request.session.get("authuser")
    no = authuser['no']

    models.insert(title, contents, '0', '1', '1', '0', no)
    
    return redirect("/board")


def updateform(request):
    no = request.GET["no"]
    result = models.findby_no(no)
    data = {"board": result}

    return render(request, 'board/view.html', data)


def update(request):
    pass

# def updateform(request):
#     # Access Control (접근 제어) - url 직접접근 막음
#     authuser = request.session.get("authuser")
#     if authuser is None:
#         return redirect('/')
#     # authuser = request.session['authuser']
#     result = models.findbyno(authuser['no'])
#     return render(request, 'user/updateform.html', result)



def deleteform(request):
    return render(request, 'board/deleteform.html')

def delete(request):
    no = request.POST["no"]
    models.deleteby_no(no)

    return redirect("/board")