from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'enrollments', views.EnrollmentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    # Students
    path('', views.student_list, name='student_list'),
    path('student/update/<int:pk>/', views.student_update, name='student_update'),
    path('student/delete/<int:pk>/', views.student_delete, name='student_delete'),
    
    # Teachers
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teacher/update/<int:pk>/', views.teacher_update, name='teacher_update'),
    path('teacher/delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),

    # Courses
    path('courses/', views.course_list, name='course_list'),
    path('course/update/<int:pk>/', views.course_update, name='course_update'),
    path('course/delete/<int:pk>/', views.course_delete, name='course_delete'),

    # Enrollments
    path('enroll/', views.enroll_student, name='enroll_student'),
    path('enroll/update/<int:pk>/', views.enrollment_update, name='enrollment_update'),
    path('enroll/delete/<int:pk>/', views.enrollment_delete, name='enrollment_delete'),
]