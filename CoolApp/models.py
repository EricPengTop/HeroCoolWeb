# coding:utf-8

# python manage.py makemigrations
# python manage.py migrate

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
class User(models.Model):
    name = models.CharField(u'姓名', max_length=30)
    password = models.CharField(u'密码', max_length=36)
    sex = models.IntegerField(u'性别')
    birthday = models.DateField(u'出生日期')

    def __unicode__(self):
        return self.name


@python_2_unicode_compatible
class News(models.Model):
    title = models.CharField(u'标题', max_length=100)
    content = models.TextField(u'内容', max_length=10000)
    pub_time = models.DateTimeField(u'发布时间')
    pub_person = models.CharField(u'发布人', max_length=30)

    def __str__(self):
        return self.title


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __unicode__(self):
        return self.full_name


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter)

    def __unicode__(self):
        return self.headline


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


# 音乐家
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
