from django.urls import path

from Studen_app import views

urlpatterns = [
    path('',views.register_students,name='register_students'),
    path('student_list',views.student_list,name='student_list'),
    path('edit_student/<int:id>',views.edit_student,name='edit_student'),
    path('delete_student/<int:id>',views.delete_student,name='delete_student'),
    path('student_dashboard/<int:id>',views.student_dashboard,name='student_dashboard'),
]