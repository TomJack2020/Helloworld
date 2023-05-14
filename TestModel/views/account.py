
from django.shortcuts import render
from django import forms
from TestModel import models


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(label="密码")



class LoginModelsForm(forms.Form):
    class Meta:
        model = models.Admin
        fields = ['username', 'password']
