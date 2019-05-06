from django.shortcuts import render

from rest_framework import generics

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , viewsets
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from . models import *
from . serializers import *
from django.shortcuts import redirect


class InstituteList(viewsets.ModelViewSet):
#    def get(self,request):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer
#    def post(self):
#        pass    

class StudentList(viewsets.ModelViewSet):
#    def get(self,request):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
#    def post(self):
#        pass    


class CourseList(viewsets.ModelViewSet):
    #def get(self,request):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # def post(self):
    #     pass    

class TeacherList(viewsets.ModelViewSet):
    #def get(self,request):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    @action(detail=False, methods=['POST'])
    def login(self, request):
        useremail = request.POST.get('email')
        userpassword = request.POST.get('password')

        user = Teacher.objects.filter(email=useremail, password=userpassword)
        n=user[0].name
        if user.count() == 0:
            return Response('user not found')
        else:
            print("pakistan")
            response = redirect('/teacher/?tname='+n)
            return response

            # return Response('You are login')

    # def post(self):
    #     pass    

class AttendanceSheetList(viewsets.ModelViewSet):
    
    queryset = AttendanceSheet.objects.all()
    serializer_class = AttendanceSheetSerializer
    def create(self, request, *args, **kwargs):
        i_name=useremail = request.POST.get('tname')
        response = super(AttendanceSheetList, self).create(request, *args, **kwargs)
        
        tmp=AttendanceSheet.objects.all().order_by('sheet_id').reverse().values_list('sheet_id')
        # tmp=tmp[0].values_list('sheet_id')
    

        c=AttendanceSheet.objects.filter(sheet_id=tmp[0][0]).values_list('crs_tchr_id')[0][0]
        c=CourseTeacher.objects.filter(id=c).values_list('tchr_id')[0][0]
        c=Teacher.objects.filter(id=c).values_list('name')[0][0]
        
        # print(tmp[0][0],"**",c)
        # here may be placed additional operations for
        # extracting id of the object and using reverse()
        return redirect('/teacher/fascript/?tname='+c+"&&tsheet="+str(tmp[0][0]))



class AttendanceList(viewsets.ModelViewSet):
    #def get(self,request):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    # def post(self):
    #     pass    

class EnrolledCourseList(viewsets.ModelViewSet):
    #def get(self,request):
    queryset = EnrolledCourse.objects.all()
    serializer_class = EnrolledCourseSerializer

    # def post(self):
    #     pass

class CourseTeacherList(viewsets.ModelViewSet):
    #def get(self,request):
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer

    # def post(self):
    #     pass

# Create your views here.

