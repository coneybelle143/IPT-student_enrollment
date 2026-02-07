from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Student, Teacher, Course, Enrollment
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer, EnrollmentSerializer
from .forms import StudentForm, TeacherForm, CourseForm, EnrollmentForm

# --- API ViewSets (Keep these for your instructor) ---
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# --- STUDENT VIEWS ---
def student_list(request):
    students = Student.objects.filter(is_active=True)
    form = StudentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/student_list.html', {'students': students, 'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.is_active = False
    student.save()
    return redirect('student_list')

# --- TEACHER VIEWS ---
def teacher_list(request):
    teachers = Teacher.objects.all()
    form = TeacherForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('teacher_list')
    return render(request, 'students/teacher_list.html', {'teachers': teachers, 'form': form})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(request.POST or None, instance=teacher)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('teacher_list')
    return render(request, 'students/teacher_form.html', {'form': form})

def teacher_delete(request, pk):
    get_object_or_404(Teacher, pk=pk).delete()
    return redirect('teacher_list')

# --- COURSE VIEWS ---
def course_list(request):
    courses = Course.objects.all()
    form = CourseForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'students/course_list.html', {'courses': courses, 'form': form})

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'students/course_form.html', {'form': form})

def course_delete(request, pk):
    get_object_or_404(Course, pk=pk).delete()
    return redirect('course_list')

# --- ENROLLMENT VIEWS ---
def enroll_student(request):
    enrollments = Enrollment.objects.all()
    form = EnrollmentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('enroll_student')
    return render(request, 'students/enrollment_list.html', {'enrollments': enrollments, 'form': form})

def enrollment_update(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    form = EnrollmentForm(request.POST or None, instance=enrollment)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('enroll_student')
    return render(request, 'students/enrollment_form.html', {'form': form})

def enrollment_delete(request, pk):
    get_object_or_404(Enrollment, pk=pk).delete()
    return redirect('enroll_student')