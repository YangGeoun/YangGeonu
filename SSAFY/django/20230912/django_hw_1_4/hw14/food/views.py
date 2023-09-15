from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'menus' : ['떡볶이', '라면', '마라탕', '쫄면', '돈까스'],
        'users' : [],
        'today' : []
    }
    return render(request, 'food/index.html', context)