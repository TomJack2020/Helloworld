# _*_ coding: utf-8 _*_
# @Time : 2023/4/25 20:56
# @Author : cep
# @Version：V 0.1
# @File : urls.py


from django.urls import path, re_path, include
from TestModel.views import views

urlpatterns = [

    # re_path('^index/?P<year>[0-9]{4}/$', views.index, name='index'),
    # re_path(r"^login/([0-9]{2})/$", views.login, name="login"),
    path("login/", views.login, name="login"),
    path("index/", views.index, name="index"),
    path("add/people/", views.add_people, name="add_people"),
    path("edit/people/", views.edit_people, name="edit_people"),
    path("delete/people/", views.delete_people, name="delete_people"),
    path("filter/people/", views.filter_people, name="filter_people"),

]
