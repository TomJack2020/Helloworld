"""
URL configuration for Helloworld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from . import views, testdb, search, search2


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    # url(r'^$', views.hello),
    # path('hello/', views.hello),
    # path('runoob/', views.runoob),
    # path('runoob1/', views.runoob1),
    # path('runoob2/', views.runoob2),
    # path('jdata/', views.json_data),
    # path('testdb/', testdb.testdb),


    path('search_form/', search.search_form),
    path('search/', search.search),
    path('search-post/', search2.search_post),
    # path('TestModel/', include(('TestModel.urls', "TestModel"))), # 加上命名空间TestModel
    path('TestModel/', include(('TestModel.urls', "TestModel"))), # 加上命名空间TestModel
    path('app01/', include(('app01.urls', "app01"))), # 加上命名空间app01


    # 激活管理工具
    path('admin/', admin.site.urls),

]


