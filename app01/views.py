import json

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

from app01.models import Department, UserInfo
from app01 import models


def index(request):
    return HttpResponse("welcome to use")


def user_list(request):
    # 根据app注册顺序在每一个template中寻找
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")


def something(request):
    # 1、获取请求方式
    print(request.method)
    # 2、在url中传递参数
    print(request.GET)
    # 3、在请求体中提交数据
    print(request.POST)

    # 5、读取html的内容  渲染替换
    # return render(request, "something.html", {'title': 'gss'})

    # 6、让浏览器重定向到其他页面
    return redirect("https://www.baidu.com")


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        # 如果是post请求， 获取用户提交的数据
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'root' and password == '123':
            # return HttpResponse("登录成功")\
            return render(request, "user_list.html")
        else:

            return render(request, 'login.html', {'error_mesg': "用户名或者密码错误"})


def orm(request):
    # 测试ORM操作表中的数据
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    # Department.objects.create(title="运营部")
    #
    # UserInfo.objects.create(name="admin", password="admin123", age=19, create_time='2023-01-01 00:00:00', depart_id=1)
    # UserInfo.objects.create(name="德莱文", password="admin1233",age=18, create_time='2023-01-02 00:00:00', depart_id=2)
    # UserInfo.objects.create(name="盖伦", password="admin123", age=18, create_time='2023-01-02 00:00:00', depart_id=2)
    # UserInfo.objects.create(name="龙龟", password="admin123", age=18, create_time='2023-01-02 00:00:00', depart_id=2)

    # 1 删除数据
    # UserInfo.objects.filter(id=3).delete()
    # UserInfo.objects.all().delete()

    # 2 获取数据 data_list = [行,行,行] QuerySet类型
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.age, obj.size, obj.data)
    # 获取第一条数据对象
    # row_obj = UserInfo.objects.filter(id=1).first()
    # print(row_obj)

    # 4 更新数据
    # UserInfo.objects.filter(id=1).update(age=999)
    # UserInfo.objects.filter(name='德莱文').update(data=3999)

    return HttpResponse("成功")


def user_list(request):
    # 1、获取数据库中所有的用户信息
    data_list = UserInfo.objects.all()
    print(data_list)

    # 2、渲染返回给用户界面
    return render(request, "user_list.html", {'data_list': data_list})


def add_list(request):
    if request.method == 'GET':
        return render(request, "add_list.html")
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        age = request.POST.get('age')
        size = request.POST.get('size')
        data = request.POST.get('data')
        print(request.POST)

        # 添加到数据库
        UserInfo.objects.create(name=user, password=pwd, age=age)

        return redirect("/app01/info/list/")
        # return render(request, "add_list.html")


def depart_list(request):
    # 部门列表
    depart_li = Department.objects.all()
    return render(request, "depart_list.html", {'depart_list': depart_li})


def depart_add(request):
    # 部门列表
    if request.method == 'GET':
        return render(request, "depart_add.html")

    print("POST")
    title = request.POST.get('title')
    print(title)
    Department.objects.create(title=title)

    # 重定向回部门列表
    return redirect("/app01/depart/list/")


def depart_delete(request):
    # 删除部门
    nid = request.GET.get('nid')
    Department.objects.filter(id=nid).delete()

    # 跳转回列表页面
    return redirect("/app01/depart/list/")

def depart_edit(request, nid):
    # 修改部门
    # http://127.0.0.1:8000/app01/depart/1/edit/
    if request.method == "GET":
        # 根据nid 获取他的数据[obd, ]
        row_obj = Department.objects.filter(id=nid).first()
        print(row_obj.id, row_obj.title)
        return render(request, "depart_edit.html", {'row_obj': row_obj})

    new_title = request.POST.get('title')
    Department.objects.filter(id=nid).update(title=new_title)
    # 跳转回列表页面
    return redirect("/app01/depart/list/")
