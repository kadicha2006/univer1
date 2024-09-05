from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'faculty_name', 'description']


class ProfessorSerializers(serializers.ModelSerializer):
    department = serializers.StringRelatedField()

    class Meta:
        model = Professor
        fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    department = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = ['id', 'user', 'department', 'enrollment_date', 'graduation_date']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student


class CourseSerializers(serializers.ModelSerializer):
    professor = ProfessorSerializers()

    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'description', 'department', 'professor']


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ScheduleSerializers(serializers.ModelSerializer):
    course = CourseSerializers()
    classroom = RoomSerializers()
    day_of_week = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ['id', 'course', 'classroom', 'start_time', 'end_time', 'day_of_week']

    def get_day_of_week(self, obj):
        return obj.get_day_of_week_display()


class AppointmentSerializers(serializers.ModelSerializer):
    student = StudentSerializers()
    course = CourseSerializers()

    class Meta:
        model = Appointment
        fields = ['id', 'student', 'course', 'date_enrolled', 'grade']
