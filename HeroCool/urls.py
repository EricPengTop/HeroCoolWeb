"""HeroCool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import CoolApp.views as views
import ShopApp.views as shop_views
import TestApp.views as test_views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^login_one_method/$', views.login_one_method),
    url(r'^login_two_method/(\S+)/(\S+)/$', views.login_two_method),
    url(r'product/create/$', shop_views.create_product),
    url(r'product/list/$', shop_views.list_product),
    url(r'test/student_list/$', test_views.student_list),
    url(r'test/student_list2/$', test_views.student_list2),
]
