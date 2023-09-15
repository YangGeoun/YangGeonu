from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('page/1/', views.page1, name='page1'),
    path('page/2/', views.page2, name='page2'),

]
