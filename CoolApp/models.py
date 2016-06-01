# coding:utf-8
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(u'姓名', max_length=30)
    password = models.CharField(u'密码', max_length=36)
    sex = models.IntegerField(u'性别')
    birthday = models.DateField(u'出生日期')

    def __unicode__(self):
        return self.name
