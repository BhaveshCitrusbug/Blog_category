from django.urls import path
from .views import base,blog_add,blog_list,delete,view_blog

urlpatterns = [
    path('base/',base,name='base'),
    path('blog_add/',blog_add,name="blog_add"),
    path('index/',blog_list,name='index'),
    path('index/<str:name>/',blog_list,name='category'),
    path('index/<str:name>/<str:datef>/<str:datet>/',blog_list,name="date_category"),
    path('index/<str:name>/<str:search>/',blog_list,name="search_category"),
    path('index/<str:name>/<str:search>/<str:datef>/<str:datet>/',blog_list,name="search_category_date"),
    path("delete/<int:id>/",delete,name="delete"),
    path('view/<int:id>/',view_blog,name='view'),



]