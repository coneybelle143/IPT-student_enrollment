from django.contrib import admin
from .models import Student, Teacher, Course, Enrollment

# This allows you to add enrollments directly inside the Student page
class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'is_active')
    list_editable = ('is_active',) # Toggle soft-delete directly from the list!
    search_fields = ('fullname', 'email')
    inlines = [EnrollmentInline]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'department')
    search_fields = ('teacher_name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'units', 'teacher')
    list_filter = ('teacher',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')
    list_filter = ('course', 'enrollment_date')