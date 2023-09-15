from django.shortcuts import render

# Create your views here.
def hello(request):
    
    context = {
        'name' : request.GET.get('username'),
        'fruits' : ['apple','samsung','banana','kakao']
    }
    return render(request, 'articles/hello.html', context)

def name_from(request):
    return render(request,'articles/throw.html')