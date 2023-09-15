from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "articles/index.html")

def throw(request):
    return render(request, "articles/throw.html")

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
        'a' : [1,2,3,4,5],
    }
    return render(request, "articles/catch.html", context)

def catchh(request,name):
    context = {
        'name' : name
    }
    return render(request, "articles/catchh.html",context)