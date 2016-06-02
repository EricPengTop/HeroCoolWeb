# coding:utf-8

from django.http.response import HttpResponse
from django.shortcuts import render
from CoolApp.forms import LoginForm


# Create your views here.
def show(request):
    return HttpResponse("你好世界!!!")


# 登录方法一(name=xxx&password=xxx)
def login_one_method(request):
    name = request.GET.get('name', None)
    password = request.GET.get('password', None)
    if name == '819598700@qq.com':
        if password == 'EricPengTop416529()':
            result = '登陆成功!!!'
        else:
            result = '登陆失败,密码错误!!!'
    else:
        result = '登陆失败,账户错误!!!'
    return HttpResponse(result)


# 登录方法二(xxx/xxx)
def login_two_method(request, name, password):
    if name == '819598700@qq.com':
        if password == 'EricPengTop416529()':
            result = '登陆成功!!!'
        else:
            result = '登陆失败,密码错误!!!'
    else:
        result = '登陆失败,账户错误!!!'
    return HttpResponse(result)


# 主页
def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            if name == 'pengtao':
                if password == '123456':
                    result = '登陆成功!!!'
                else:
                    result = '登陆失败,密码错误!!!'
            else:
                result = '登陆失败,账户错误!!!'
            return HttpResponse(result)
    else:
        string = u'你好世界，你好Python，你好Django，你好我自己！！！'
        studyList = ['HTML', 'JS', 'CSS', 'JQuery', 'Python', 'Django']
        content_info = {'name': u'pengtao', 'password': u'123456'}
        list = map(str, range(100))
        return render(request, 'home.html', {'str': string, 'studyList': studyList, 'content_info': content_info, 'list': list})
