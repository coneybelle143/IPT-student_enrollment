from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('enroll/', views.enroll_student, name='enroll_student'),
    path('edit/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('teacher/edit/<int:pk>/', views.teacher_update, name='teacher_update'),
    path('teacher/delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),
    path('course/edit/<int:pk>/', views.course_update, name='course_update'),
    path('course/delete/<int:pk>/', views.course_delete, name='course_delete'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('courses/', views.course_list, name='course_list'),
    path('enroll/delete/<int:pk>/', views.enrollment_delete, name='enrollment_delete'),
    path('enroll/', views.enroll_student, name='enroll_student'),
    path('enroll/edit/<int:pk>/', views.enrollment_update, name='enrollment_update'),
    path('enroll/delete/<int:pk>/', views.enrollment_delete, name='enrollment_delete'),
]