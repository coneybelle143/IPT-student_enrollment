from django import forms
from .models import Student, Enrollment, Teacher, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fullname', 'email']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_name', 'department']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'units', 'teacher']