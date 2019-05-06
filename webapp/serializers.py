from rest_framework import serializers
from .models import *

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institute
        fields='__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'
class AttendanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=AttendanceSheet
        fields='__all__'
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'
class EnrolledCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=EnrolledCourse
        fields='__all__'
class CourseTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseTeacher
        fields='__all__'

