from django.db import models

from django.contrib.auth.models import User

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin_profile")  # Link to User
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Store plain text temporarily (will be hashed)

    def _str_(self):
        return self.name

    def save(self, *args, **kwargs):
        """Ensure that when an Admin is created, a User object is also created with the given password."""
        if not self.user:
            # Create a user with the provided password
            user = User.objects.create_user(username=self.email, email=self.email, password=self.password)
            user.is_staff = True  # Mark as staff but not superuser
            user.save()
            self.user = user  # Link the created user
        else:
            # If password is updated in the Admin model, update it in the User model
            self.user.set_password(self.password)
            self.user.save()
        super().save(*args, **kwargs)

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