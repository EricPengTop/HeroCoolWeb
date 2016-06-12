from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=36)
    sex = models.IntegerField()
    birthday = models.DateField(auto_now=timezone.now())

    class Meta:
        abstract = True


class Student(Person):
    work = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s, %s, %s, %s' % (self.name, self.sex, self.birthday, self.work)

    class Meta(Person.Meta):
        ordering = ['-birthday', 'name']
        get_latest_by = 'birthday'
