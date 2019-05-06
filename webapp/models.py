from django.db import models

class Institute(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    emailAddress = models.EmailField()
    initial = models.CharField(max_length=3)
    rollNumber = models.CharField(max_length=10)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

    def __str__(self):
        return self.fName
        
class Course(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=30)
    title=models.CharField(max_length=10)
    code=models.CharField(max_length=10)

    def __str__(self):
        return self.course_name

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name+"--"+str(self.id)
    

class CourseTeacher(models.Model):
    id = models.AutoField(primary_key=True)
    crs_Id = models.ForeignKey(Course , on_delete = models.CASCADE)
    tchr_id = models.ForeignKey(Teacher , on_delete = models.CASCADE)

    def __int__(self):
        return self.id

class AttendanceSheet(models.Model):
    sheet_id=models.AutoField(primary_key=True)
    date = models.DateField()
    startTime = models.CharField(max_length=10)
    lateTime = models.CharField(max_length=10)
    endTime = models.CharField(max_length=10)
    crs_tchr_id = models.ForeignKey(CourseTeacher , on_delete = models.CASCADE)

    def __int__(self):
        return self.sheet_id

class Attendance(models.Model):
    attendance_id=models.AutoField(primary_key=True)
    status=models.CharField(max_length=3)
    std_id = models.ForeignKey(Student , on_delete=models.CASCADE)
    AttendSheet_id = models.ForeignKey(AttendanceSheet , on_delete=models.CASCADE)

    def __int__(self):
        return self.attendance_id

class EnrolledCourse(models.Model):
    enrollcourse_id=models.AutoField(primary_key=True)
    crs_Id = models.ForeignKey(Course , on_delete = models.CASCADE)
    std_Id = models.ForeignKey(Student , on_delete = models.CASCADE)

    def __int__(self):
        return self.enrollcourse_id

# Create your models here.
