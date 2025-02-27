# Generated by Django 5.1.1 on 2024-09-06 05:34

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
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=32)),
                ('faculty_name_en', models.CharField(max_length=32, null=True)),
                ('faculty_name_ru', models.CharField(max_length=32, null=True)),
                ('faculty_name_ky', models.CharField(max_length=32, null=True)),
                ('faculty_name_tr', models.CharField(max_length=32, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_ky', models.TextField(null=True)),
                ('description_tr', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10)),
                ('building', models.CharField(max_length=50)),
                ('capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_name', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=32)),
                ('bio', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.faculty')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day_of_week', models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница')])),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.room')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField()),
                ('graduation_date', models.DateField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.faculty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateField()),
                ('grade', models.CharField(blank=True, max_length=2, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.student')),
            ],
        ),
    ]
