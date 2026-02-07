from django.db import models

# 1. Teacher Table
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.teacher_name

# 2. Student Table
class Student(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname

# 3. Course Table (Depends on Teacher)
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    units = models.IntegerField()
    # ForeignKey links a Course to a Teacher (1 Teacher -> Many Courses)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.course_name} (Instructor: {self.teacher.teacher_name})"

# 4. Enrollment Table (Links Students and Courses)
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        # ensures a student can't enroll in the same course twice
        unique_together = ('student', 'course')