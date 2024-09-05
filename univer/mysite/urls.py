from django.urls import path
from .views import *


urlpatterns = [
    path('', StudentViewSets.as_view({'get': 'list', 'post': 'create'}), name='student_list'),
    path('<int:pk>/', StudentViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name = 'faculty_detail'),

    path('faculty/', FacultyViewSets.as_view({'get': 'list', 'post': 'create'}), name='faculty_list'),
    path('faculty/<int:pk>/', FacultyViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                                           'delete': 'destroy'}), name='faculty_detail'),

    path('professor/', ProfessorViewSets.as_view({'get': 'list', 'post': 'create'}), name='professor_list'),
    path('professor/<int:pk>/', ProfessorViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='professor_detail'),

    path('course/', CourseViewSets.as_view({'get': 'list', 'post': 'create'}), name='course_list'),
    path('course/<int:pk>/', CourseViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='course_detail'),

    path('room', RoomViewSets.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
    path('room/<int:pk>/', RoomViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                                       'delete': 'destroy'}), name='room_detail'),

    path('schedule/', ScheduleViewSets.as_view({'get': 'list', 'post': 'create'}), name='schedule_list'),
    path('schedule/<int:pk>/', ScheduleViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                                       'delete': 'destroy'}), name='chedule_detail'),

    path('appointment/', AppointmentViewSets.as_view({'get': 'list', 'post': 'create'}), name='appointment_list'),
    path('appointment/<int:pk>/', AppointmentViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                                       'delete': 'destroy'}), name='appointment_detail'),
]