from django.shortcuts import render, redirect
from . import models


def index(request):
    results = models.findall()
    data = {"board_list": results}
    # print(data)
    return render(request, 'board/index.html', data)
    

def view(request):
    no = request.GET["no"]
    # print(no)
    result = models.findby_no(no)
    # print(result)
    # hit(조회수 +1 해야함)
    result["hit"] += 1
    data = {"board": result}

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


def deleteform(request):
    pass

def delete(request):
    pass

