from django.shortcuts import render, redirect
from . import models

# Create your views here.



def index(request):
    results = models.findall()
    data = {
        "guestbook_list": results
    }
    return render(request, 'guestbook/index.html', data)



def add(request):
    name = request.POST["name"]
    password = request.POST["password"]
    message = request.POST["message"]

    models.insert(name, password, message)

    return redirect("/guestbook")


def deleteform(request):
    return render(request, 'guestbook/deleteform.html')


def delete(request):
    no = request.GET['no']
    password = request.POST['password']

    models.deleteby_no_and_password(no, password)

    return redirect("/guestbook")

