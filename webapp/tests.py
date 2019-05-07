from django.test import TestCase
import time
from .models import *
# Create your tests here.

class modelTests(TestCase):

    def setUp(self):
        Institute.objects.create(id=123,name="testInstitute")
        ins=Institute.objects.get(id=123)
        Student.objects.create(id=123, fName="test",lName="test",emailAddress="test@test.com",initial="A11111",rollNumber="test",institute=ins)
        Course.objects.create(course_id=1,course_name="testcourse",title="testcourse",code="111")
        Teacher.objects.create(id=1,name="testTeacher",email="test@test.com",password="test")
        obj2=Teacher.objects.get(id=1)
        obj1=Course.objects.get(course_id=1)
        CourseTeacher.objects.create(id=1,crs_Id=obj1,tchr_id=obj2)
        obj3=CourseTeacher.objects.get(id=1)
        AttendanceSheet.objects.create(sheet_id=1,date="2019-01-01",startTime="11:00 AM",lateTime="11:10 AM" ,endTime="11:55 AM",crs_tchr_id=obj3)


    def test_student(self):
        std = Student.objects.get(id=123)
        expected = std.fName
        self.assertEqual(expected, "test")

    def test_institute(self):
        ins1 = Institute.objects.get(id=123)
        expected = ins1.name
        self.assertEqual(expected, "testInstitute")

    def test_course(self):
        crs=Course.objects.get(course_id=1)
        expected=crs.course_name
        expected2=crs.code
        self.assertEqual(expected,"testcourse")
        self.assertEqual(expected2,"111")
    
    def test_teacher(self):
        tch=Teacher.objects.get(id=1)
        expected=tch.name
        expected2=tch.password
        self.assertEqual(expected,"testTeacher")
        self.assertEqual(expected2,"test")
        self.assertEqual(tch.email,"test@test.com")
    
    def test_courseT(self):
        crsT=CourseTeacher.objects.get(id=1)
        crs=Course.objects.get(course_id=1)
        tch=Teacher.objects.get(id=1)
        expected=crsT.crs_Id
        expected2=crsT.tchr_id
        self.assertEqual(expected,crs)
        self.assertEqual(expected2,tch)

    def test_AttendanceS(self):
        crsT=CourseTeacher.objects.get(id=1)
        AttendanceS=AttendanceSheet.objects.get(sheet_id=1)
        expected=AttendanceS.crs_tchr_id
        self.assertEqual(expected,crsT)

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            #'id':2,
            #'name': 'test',
            'email': 'abc@xyz.com',
            'password': 'secret'}
        Teacher.objects.create(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
    