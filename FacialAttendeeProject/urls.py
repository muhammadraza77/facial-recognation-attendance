"""FacialAttendeeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include('webapp.urls')),
    path('teacher/', include('teacher.urls')),
    # url('student/', views.studentList.as_view()),
    # url('course/', views.courseList.as_view()),
    # url('teacher/', views.teacherList.as_view()),
    # url('attendancesheet/', views.attendancesheetList.as_view()),A
    # url('attendance/', views.attendanceList.as_view()),
    # url('enrolledcourse/', views.enrolledcourseList.as_view()),
]
