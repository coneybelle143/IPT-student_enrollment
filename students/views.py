from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Enrollment, Teacher, Course
from .forms import StudentForm, EnrollmentForm, TeacherForm, CourseForm

def student_list(request):
    students = Student.objects.filter(is_active=True)
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'students/student_list.html', {'students': students, 'form': form})

# UPDATE: Edit an existing student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

# DELETE: Remove a student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.is_active = False # Mark as inactive
        student.save() # Save the change
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})

# 1. List only inactive students
def student_trash(request):
    deleted_students = Student.objects.filter(is_active=False)
    return render(request, 'students/student_trash.html', {'students': deleted_students})

# 2. Logic to "Restore" a student
def student_restore(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.is_active = True  # Switch the flag back to True
    student.save()
    return redirect('student_list') 

def enroll_student(request):
    enrollments = Enrollment.objects.all()
    form = EnrollmentForm()
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enroll_student')
    return render(request, 'students/enrollment_list.html', {'enrollments': enrollments, 'form': form})


# --- TEACHER LIST VIEW ---
def teacher_list(request):
    teachers = Teacher.objects.filter(is_active=True)
    form = TeacherForm()
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    return render(request, 'students/teacher_list.html', {'teachers': teachers, 'form': form})

# --- COURSE LIST VIEW ---
def course_list(request):
    courses = Course.objects.filter(is_active=True)
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    return render(request, 'students/course_list.html', {'courses': courses, 'form': form})

# --- TEACHER VIEWS ---
def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(instance=teacher)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    return render(request, 'students/teacher_form.html', {'form': form})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        teacher.is_active = False
        teacher.save()
        return redirect('teacher_list')
    return render(request, 'students/student_confirm_delete.html', {'student': teacher})

# --- COURSE VIEWS ---
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(instance=course)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    return render(request, 'students/course_form.html', {'form': form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.is_active = False
        course.save()
        return redirect('course_list')
    return render(request, 'students/student_confirm_delete.html', {'student': course})

def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == "POST":
        enrollment.delete() # Permanent delete for un-enrolling
        return redirect('enroll_student')
    return render(request, 'students/student_confirm_delete.html', {'student': enrollment})

# --- ENROLLMENT VIEWS ---

# List and Create Enrollments
def enroll_student(request):
    enrollments = Enrollment.objects.all() # Fetch all current enrollments
    form = EnrollmentForm()
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enroll_student')
    return render(request, 'students/enrollment_list.html', {'enrollments': enrollments, 'form': form})

# Edit an Enrollment
def enrollment_update(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    form = EnrollmentForm(instance=enrollment)
    if request.method == "POST":
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enroll_student')
    return render(request, 'students/enrollment_form.html', {'form': form})

# Delete an Enrollment (Un-enroll)
def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == "POST":
        enrollment.delete() # Hard delete since this is un-enrolling, not archiving
        return redirect('enroll_student')
    return render(request, 'students/student_confirm_delete.html', {'student': enrollment})