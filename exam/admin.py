from django.contrib import admin

from exam.models import Exam,ExamHall,SeatAllocation,Student

admin.site.register(Exam)

admin.site.register(ExamHall)

admin.site.register(SeatAllocation)

admin.site.register(Student)


