
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',AllStudents,name="allstudents"),
    path('add/',AddStudent,name="addstudent"),
    path('edit/<int:id>/',EditStudent,name="editstudent"),
    path('delete/<int:id>/',DeleteStudent,name="deletestudent")
]