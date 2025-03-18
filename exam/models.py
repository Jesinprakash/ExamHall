from django.db import models

from django.contrib.auth.models import User

class Admin(models.Model):
    DESIGNATION_CHOICES = [
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('HOD', 'Head of Department'),
        ('Advisor', 'Advisor'),
    ]

    name = models.CharField(max_length=255)

    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)

    phone_number = models.CharField(max_length=12)

    email = models.EmailField(unique=True)

    def _str_(self):
        return self.name

class Student(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science & Engineering'),
        ('CHEM', 'Chemical Engineering'),
        ('FOOD', 'Food Technology'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")

    reg_no = models.CharField(max_length=20, unique=True)

    name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)

    phone=models.CharField(max_length=12)

    def _str_(self):
        return self.name

class ExamHall(models.Model):

    hall_name = models.CharField(max_length=255)

    floor = models.IntegerField()

    capacity = models.PositiveIntegerField()

    created_by = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name="exam_halls")

    def _str_(self):
        return self.hall_name

class Exam(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science & Engineering'),
        ('CHEM', 'Chemical Engineering'),
        ('FOOD', 'Food Technology'),
    ]

    exam_name = models.CharField(max_length=255)

    exam_date = models.DateField()

    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)

    exam_hall = models.ForeignKey(ExamHall, on_delete=models.CASCADE, related_name="exams")

    def _str_(self):
        return self.exam_name

class SeatAllocation(models.Model):

    seat_no = models.CharField(max_length=10)

    allocation_date = models.DateField(auto_now_add=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="seat_allocations")

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="seat_allocations")

    def _str_(self):
        return self.seat_no