from django.shortcuts import render

# Create your views here.

def index(request):
    # page = request.GET['p']
    # boardlist = models.findall(page)


    return render(request, 'board/index.html')
    


def view(request):
    return render(request, 'board/view.html')