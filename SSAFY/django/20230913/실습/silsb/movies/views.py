from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "movies/index.html")

def page1(request):
    return render(request, "movies/page1.html")

def page2(request):
    return render(request, "movies/page2.html")

def page(request):
    return render(request, "movies/page2.html")