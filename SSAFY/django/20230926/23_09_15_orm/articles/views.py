from django.shortcuts import render,redirect
from .models import Article
from .forms import AriticleForm

# Create your views here.
def index(request):
    #게시글 목록 조회해서 템플릿에 전달
    #1. 게시글 목록 DB에서 조회
    #    ORM 이용해야 하는데 >> 이 역할을 Model class(Article)가 수행
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }

    return render(request,'articles/index.html',context)

# def new(request):
#     form = AriticleForm()
#     context = {
#         'form' : form
#     }
#     return render(request,'articles/new.html', context)


# def create(request):
#     # 요청에서 데이터 받아와서 DB에 저장하고
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # # Article.objects.create()
#     # article = Article(title=title,content=content)
#     # article.save()
#     form = AriticleForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('articles:index',)
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html',context)



def create(request):
    if request.method == 'POST':
        form = AriticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = AriticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html',context)

def delete(request,pk):

    # DB에서 삭제하고 목록조회해서 템플릿에 전달
    # record 단위는 instance로 처리...
    article = Article.objects.get(pk=pk)
    article.delete()
    # articles = Article.objects.all()
    # context = {
    #     'articles' :articles
    # }
    # return render(request,'articles/index.html', context)
    return redirect('articles:index')

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

# def edit(request, pk):
    # article = Article.objects.get(pk=pk)
    # context = {
    #     'article' : article
    # }
    # return render(request, 'articles/update.html', context)

# def update(request,pk):
#     # 요청에서 데이터 받아와서 DB에 저장하고
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     # Article.objects.create()
#     article = Article.objects.get(pk=pk)
#     article.title = title
#     article.content = content
#     article.save()
    
#     return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = AriticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)
    else:
        form = AriticleForm(instance=article)
    context = {
        'article' : article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)
