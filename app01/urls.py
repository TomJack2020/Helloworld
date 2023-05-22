
from django.urls import path, re_path, include
from app01 import views

urlpatterns = [


    # 请求和响应
    path('something/', views.something),

    # 用户登录
    path('login/', views.login),
    path('orm/', views.orm),


    # 用户管理
    path('user/list/', views.user_list),
    path('info/add/', views.add_list),

    # 部门管理
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/edit/', views.depart_edit),

    # 用户管理
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/modelform/add/', views.user_modelform_add),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/<int:nid>/delete/', views.user_delete),



    # 靓号管理
    path('pretty/list/', views.pretty_list),
    path('pretty/add/', views.pretty_add),
    path('pretty/<int:nid>/edit/', views.pretty_edit),
    path('pretty/<int:nid>/delete/', views.pretty_delete),








]
