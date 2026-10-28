from django.urls import path

from Studen_app import views

urlpatterns = [
    path('',views.register_students,name='register_students'),
    path('student_list',views.student_list,name='student_list'),
    path('edit_student',views.edit_student,name='edit_student'),
    path('delete_student',views.delete_student,name='delete_student'),
]