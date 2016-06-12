from django.shortcuts import render
from TestApp.models import Student
import MySQLdb


# Create your views here.
def student_list(request):
    db = MySQLdb.connect(user='root', passwd='Tao416()', db='python_study')
    cursor = db.cursor()
    cursor.execute('select * from student order by sex')
    result = cursor.fetchall()
    db.close()
    context = {'title': 'student list', 'result': result}
    return render(request, 'testapp/student_list.html', context)


def student_list2(request):
    student = Student.objects.all()
    return render(request, 'testapp/student_list.html', {'result': student})

