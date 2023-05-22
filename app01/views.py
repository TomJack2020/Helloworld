import json
import math

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

from app01.models import Department, UserInfo
from app01 import models
from django.utils.safestring import mark_safe


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
    # # 部门列表
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


# 用户管理
def user_list(request):
    queryset = UserInfo.objects.all()
    return render(request, "user_list.html", {'data_list': queryset})


def user_add(request):
    if request.method == 'GET':
        context = {
            'gender_choice': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all()

        }
        return render(request, 'user_add.html', context)

    # 获取用户信息

    name = request.POST.get('username')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gd')
    depart_id = request.POST.get('dp')

    # 添加到数据库
    models.UserInfo.objects.create(name=name, password=pwd, age=age, account=account,
                                   create_time=ctime, gender=gender, depart_id=depart_id)
    print(ctime)
    return redirect('/app01/user/list/')


# ===========================================================================
from django import forms


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart']

        # widgets = {
        #     'name': forms.TextInput(attrs={"class":"form-control"}),
        #     'password': forms.PasswordInput(attrs={"class":"form-control"})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, filed in self.fields.items():
            print(name, filed)
            filed.widget.attrs = {'class': 'form-control', 'placeholder': filed.label}


def user_modelform_add(request):
    """添加用户 基于ModelForm"""

    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_modelform_add.html', {'form': form})

    # 用户POST提交数据  数据校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法 保存到数据库
        form.save()
        return redirect('app01/user/list/')
    # 校验失败 在页面显示错误信息
    else:

        return render(request, 'user_modelform_add.html', {'form': form})


def user_edit(request, nid):
    """编辑用户"""
    row_object = models.UserInfo.objects.filter(id=nid).first()
    form = UserModelForm(instance=row_object)

    if request.method == "GET":
        return render(request, "user_edit.html", {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/app01/user/list')
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, nid):
    """删除用户"""
    row_object = models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/app01/user/list/')


# 靓号管理

class PrettyModelForm(forms.ModelForm):
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, filed in self.fields.items():
            print(name, filed)
            filed.widget.attrs = {'class': 'form-control', 'placeholder': filed.label}


def pretty_list(request):
    """靓号列表"""

    """测试创建测试数据"""
    # for i in range(100):
    #     models.PrettyNum.objects.create(mobile='12267834567', price=10, level=1, status=2)

    # queryset = models.PrettyNum.objects.all().order_by('-level')  # -lever  DESC  level
    """搜索"""
    # # 搜索
    # models.PrettyNum.objects.filter(id=12)  # 等于12
    # # 字典搜索 如果字典为空则是全部
    # # data_dict = {'mobile': '13475623471', 'id': 12}
    # # models.PrettyNum.objects.filter(**data_dict)  #
    #
    # # 搜索条件 id
    # models.PrettyNum.objects.filter(id__gt=12)  # 大于12
    # models.PrettyNum.objects.filter(id__gte=12)  # 大于等于12
    # models.PrettyNum.objects.filter(id__lt=12)  # 小于12
    # models.PrettyNum.objects.filter(id__lte=12)  # 小于等于12
    #
    # # 搜索条件  字符串
    # models.PrettyNum.objects.filter(mobile="999")  # mobile='999'
    # models.PrettyNum.objects.filter(mobile__startswith="999")  # mobile 以'999' 开头
    # models.PrettyNum.objects.filter(mobile__endswith="999")  # mobile 以'999' 结尾
    # models.PrettyNum.objects.filter(mobile__contains="999")  # mobile 包含'999'
    #
    # # 测试
    # res = models.PrettyNum.objects.filter(mobile__contains="139")  # mobile 以'xxx' 结尾
    # print(res)

    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict['mobile__contains'] = search_data

    # 1、根据用户想要访问的页计算 分页数据
    page = int(request.GET.get('page', ''))
    start = (page - 1) * 10
    end = page * 10
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by('-level')[start:end]

    # 页码
    page_str_list = []
    for i in range(1, 21):
        ele = f'<li><a href="/app01/pretty/list/?page={i}">{i}</a></li>'
        page_str_list.append(ele)

    page_string = mark_safe("".join(page_str_list))

    return render(request, "pretty_list.html",
                  {'queryset': queryset, 'search_data': search_data, 'page_string': page_string})


def pretty_add(request):
    """新建靓号"""

    if request.method == 'GET':
        form = PrettyModelForm()
        return render(request, "pretty_add.html", {'form': form})

    form = PrettyModelForm(data=request.POST)

    # 提交后数据校验并返回靓号列表
    if form.is_valid():
        form.save()
        return redirect("/app01/pretty/list/")
    return render(request, "pretty_add.html", {'form': form})


def pretty_edit(request, nid):
    """编辑靓号"""
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    form = PrettyModelForm(instance=row_object)

    if request.method == "GET":
        return render(request, "pretty_edit.html", {'form': form})

    form = PrettyModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/app01/pretty/list')
    return render(request, 'pretty_edit.html', {'form': form})


def pretty_delete(request, nid):
    """删除靓号 操作"""
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/app01/pretty/list/')
