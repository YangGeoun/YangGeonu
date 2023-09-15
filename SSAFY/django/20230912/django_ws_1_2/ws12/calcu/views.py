from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, "calcu/calculation.html")

# Create your views here.
def catch(request):
    f_num = int(request.GET.get('f_num'))
    s_num = int(request.GET.get('s_num'))
    context = {
        'f_num' : f_num,
        's_num' : s_num,
    }
    return render(request, "calcu/result.html", context)