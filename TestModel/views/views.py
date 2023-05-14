import json

from django.shortcuts import render, redirect, reverse

# Create your views here.

from django.shortcuts import HttpResponse
from TestModel import models


def login(request):
    # 判断到底是POST还是GET请求
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        # 去请求体中取数据
        # return HttpResponse('Have an error')
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')

        print(username, pwd)

        # 去数据库中校验 用户名和账号密码

        # 成功跳转到后台管理界面
        if (username == 'admin') and (pwd == 'admin'):
            return redirect('/index/')
        # 失败 则重新输入  -> 用户名或密码错误
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})


def index(request):
    # return HttpResponse("welcome:" + "123")
    # 数据库数据筛选
    # queryset = models.People.objects.all().order_by('-id') # asc
    queryset = models.People.objects.all().order_by('-id')  # desc
    # queryset =[
    #     {'id':1, 'name': 1233, 'city':'wuhan'},
    #     {'id':2, 'name': 1233, 'city':'wuhan'},
    #     {'id':3, 'name': 1233, 'city':'wuhan'},
    #     {'id':4, 'name': 1233, 'city':'wuhan'},
    #     {'id':5, 'name': 1233, 'city':'wuhan'},
    #     {'id':6, 'name': 1233, 'city':'wuhan'}
    # ]
    # 展示渲染
    return render(request, 'index.html', {'queryset': queryset})


def add_people(request):
    if request.method == 'GET':
        return render(request, 'add_people.html')
    else:
        # 提交信息新建
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        age = request.POST.get('age')
        models.People.objects.create(name=name, gender=gender, city=city, age=age)
        # 跳转回到列表页面
        return redirect('/index/')


def delete_people(request):
    people_id = request.GET.get('id')
    models.People.objects.filter(id=people_id).delete()
    print(people_id)

    return redirect('/index/')


def edit_people(request):
    """编辑页面"""

    # 从列表页面跳转过来的时候
    if request.method == 'GET':
        people_id = request.GET.get('id')
        people_object = models.People.objects.filter(id=people_id).first()
        return render(request, 'edit_people.html', {'people_object': people_object})
    else:
        # # 编辑和提交数据
        people_id = request.GET.get("id")
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        age = request.POST.get('age')

        # 修改数据
        models.People.objects.filter(id=people_id).update(name=name, gender=gender, city=city, age=age)
        return redirect('/index/')


def filter_people(request):
    """编辑页面"""

    # 从列表页面跳转过来的时候
    if request.method == 'GET':
        people_id = request.GET.get('search')
    else:
        people_id = request.POST.get('search')
        # print(people_id)
    # queryset = models.People.objects.filter(id__gt=people_id) # id 大于people_id
    queryset = models.People.objects.filter(id=people_id) # id等于people_id
    return render(request, 'index.html', {'queryset': queryset})
