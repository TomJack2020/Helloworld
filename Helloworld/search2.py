# _*_ coding: utf-8 _*_
# @Time : 2023/4/25 20:35
# @Author : cep
# @Version：V 0.1
# @File : search2.py

from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
