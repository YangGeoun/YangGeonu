from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index,name='index'),
    path('<int:pk>/',views.detail , name='detail'),
    path('new/',views.new , name='new'),
    path('create/',views.create , name='create'),
    path('delete/<int:pk>/',views.delete , name='delete'),
    path('edit/<int:pk>/',views.edit , name='edit'),
    path('update/<int:pk>/',views.update , name='update'),
    
]
