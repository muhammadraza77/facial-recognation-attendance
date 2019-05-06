from django.contrib import admin

from . models import Student
from . models import Institute
from . models import Course
from . models import Teacher
from . models import AttendanceSheet
from . models import Attendance
from . models import EnrolledCourse
from . models import CourseTeacher

admin.site.register(Student)
admin.site.register(Institute)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(AttendanceSheet)
admin.site.register(Attendance)
admin.site.register(EnrolledCourse)
admin.site.register(CourseTeacher)

# Register your models here.
