from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.faculty_name


class Professor(models.Model):
    prof_name = models.CharField(max_length=32)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    bio = models.TextField()

    def __str__(self):
        return self.prof_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    description = models.TextField()
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    building = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f'Room {self.room_number}'


class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    DAYS_OF_WEEK = [
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Четверг'),
        (5, 'Пятница'),
    ]

    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK)

    def __str__(self):
        return self.course.name


class Appointment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    grade = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return f'{self.student} - {self.course}'