# _*_ coding: utf-8 _*_
# @Time : 2023/4/24 20:01
# @Author : cep
# @Version：V 0.1
# @File : views.py
import json
from django.http import HttpResponse
from django.shortcuts import render
import datetime


def hello(request):
    return HttpResponse("welcome to our system")


def runoob(request):
    context = {'hello': 'Hello world'}
    return render(request, 'runoob.html', context)


def runoob1(request):
    view_name = 'my name is 100 Net'
    pub_date = datetime.datetime.now()
    num = 10240
    dic = {"name": view_name,
           "pub_date": pub_date,
           "num": num}
    return render(request, 'runoob.html', dic)


def runoob2(request):
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    return render(request, "runoob.html", {"views_str": views_str})


def json_data(request):
    # if request.method == "GET":
    #     result = {}
    #     sku = request.GET.get('sku')
    #     result['sku'] = sku
    #     result = json.dumps(result)
    #     return HttpResponse(result)
    # else:
    #     render(request, 'login111.html')

    li = [
        {'name': 'tom', 'age': 18, 'sex': 1},
        {'name': 'tom', 'age': 18, 'sex': 1},
        {'name': 'tom', 'age': 18, 'sex': 1},
        {'name': 'tom', 'age': 18, 'sex': 1}
          ]
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': li}
    result = json.dumps(return_dict)
    return HttpResponse(result)







