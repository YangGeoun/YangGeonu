from django.shortcuts import render
from . import models

# Create your views here.
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = models.Article()
    article.title = title
    article.content = content
    article.save()
    return render(request, 'articles/create.html')