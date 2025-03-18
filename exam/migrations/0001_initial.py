# Generated by Django 5.1.7 on 2025-03-16 23:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(choices=[('Associate Professor', 'Associate Professor'), ('Assistant Professor', 'Assistant Professor'), ('HOD', 'Head of Department'), ('Advisor', 'Advisor')], max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExamHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(max_length=255)),
                ('floor', models.IntegerField()),
                ('capacity', models.PositiveIntegerField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_halls', to='exam.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=255)),
                ('exam_date', models.DateField()),
                ('department', models.CharField(choices=[('CSE', 'Computer Science & Engineering'), ('CHEM', 'Chemical Engineering'), ('FOOD', 'Food Technology')], max_length=20)),
                ('exam_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='exam.examhall')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('department', models.CharField(choices=[('CSE', 'Computer Science & Engineering'), ('CHEM', 'Chemical Engineering'), ('FOOD', 'Food Technology')], max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeatAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.CharField(max_length=10)),
                ('allocation_date', models.DateField(auto_now_add=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_allocations', to='exam.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_allocations', to='exam.student')),
            ],
        ),
    ]
