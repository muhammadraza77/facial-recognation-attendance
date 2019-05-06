from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from webapp.models import *
from fascript import *
from fascript.identify_faces import foo
from django.shortcuts import redirect
# from webapp.models import CourseTeacher
# Create your views here.

# Create your views here.
def index(request):
    i_name=request.GET.get('tname', '')
    # i_name='Nauman Ghazi'

    tid= Teacher.objects.filter(name=i_name).values('id')
    courses = CourseTeacher.objects.filter(tchr_id=tid.get()['id']).values('crs_Id','id')
    totalStudent = 0
    totalSheets = 0
    for course in courses:
        totalStudent += EnrolledCourse.objects.filter(crs_Id=course['crs_Id']).count()
        totalSheets += AttendanceSheet.objects.filter(crs_tchr_id = course['id']).count()

    template=loader.get_template('teacher/dashboard.html')
    
    context={
        'a': i_name,
        'b': courses.count(),
        'c': totalStudent,
        'd': totalSheets,
        'e': "http://localhost:8000/teacher/addAttendance/?tname="+i_name,
    }
    print(context)
    return HttpResponse(template.render(context,request))

def addsheet(request):
    i_name='Nauman Ghazi'
    i_name=request.GET.get('tname', '')
    tid= Teacher.objects.filter(name=i_name).values('id')
    courses = CourseTeacher.objects.filter(tchr_id=tid.get()['id']).values('crs_Id')
    coursesList = []
    for course in courses:
        op=Course.objects.filter(course_id = course['crs_Id']).values_list('course_name','course_id')
        op1=CourseTeacher.objects.filter(tchr_id=tid.get()['id'])
        op1=CourseTeacher.objects.filter(crs_Id=op[0][1]).values_list('id')
        
        print(i_name,"**")
        myobj={
            'cname':op[0][0],
            'cid':op1[0][0],
        }
        coursesList.append(myobj)

    template=loader.get_template('teacher/addsheet.html')
    print(coursesList)
    context={
        'tname':i_name,
        'a' : coursesList,
        'viewsheet': "http://localhost:8000/teacher/viewsheet/?tname="+i_name+"&tsheet=1",
        'dashboard': "http://localhost:8000/teacher/?tname="+i_name,
    }
    
    return HttpResponse(template.render(context,request))    

def login(request):
    # i_name='Nauman Ghazi'

    # tid= Teacher.objects.filter(name=i_name).values('id')
    # courses = CourseTeacher.objects.filter(tchr_id=tid.get()['id'])

    # tid= Teacher.objects.filter(name=i_name).values('id')
    # courses = CourseTeacher.objects.filter(tchr_id=tid.get()['id'])

    template=loader.get_template('teacher/login.html')

    context={

    }
    
    return HttpResponse(template.render(context,request))

def signup(request):
    # i_name='Nauman Ghazi'

    # tid= Teacher.objects.filter(name=i_name).values('id')
    # courses = CourseTeacher.objects.filter(tchr_id=tid.get()['id'])

    # tid= Teacher.objects.filter(name=i_name).values('id')
    # courses = CourseTeacher.objects.filter(tchr_id=tid.get()['id'])

    template=loader.get_template('teacher/signup.html')
    
    context={
    }
    
    return HttpResponse(template.render(context,request))

def viewsheet(request):
    # i_name='Nauman Ghazi'
    i_name=request.GET.get('tname', '')
    i_sheetid=request.GET.get('tsheet', '')
    i_sheetid=int(i_sheetid)

    mylist=[]

    pp=Attendance.objects.filter(AttendSheet_id=i_sheetid).values_list('std_id','status')

    # p1=Student.objects.filter(name=).values_list('std_id','status')

    for p2 in pp:
        # print(p2[0],"***",p2[1])
        stid = p2[0]
        status=p2[1]
        sname=Student.objects.filter(id=stid).values_list('fName','lName')
        
        # print(stid,'*',status,'*',sname[0][0],'*',sname[0][1])
        if status=='P':
            s='gbtn'
        else:
            s='rbtn'
        # temp='<td><button class="'+s+'">'+status+'</button></td>'
        myObj={
            'id':stid,
            'status':status,
            'cls':s,
            'name':sname[0][0]+" "+sname[0][1],
        }
        mylist.append(myObj)

    # print(mylist)

    template=loader.get_template('teacher/viewsheet.html')
#################################333
    tid= Teacher.objects.filter(name=i_name).values('id')
    
    courses = CourseTeacher.objects.filter(tchr_id=tid.get()['id']).values('crs_Id')
    coursesList = []
    for course in courses:
        op=Course.objects.filter(course_id = course['crs_Id']).values_list('course_name','course_id')
        op1=CourseTeacher.objects.filter(tchr_id=tid.get()['id'])
        op1=CourseTeacher.objects.filter(crs_Id=op[0][1]).values_list('id')
        
        # print(i_name,"**")
        myobj={
            'cname':op[0][0],
            'cid':op1[0][0],
        }
        coursesList.append(myobj)
######################################33
    context={
        'a':i_name,
        'b':mylist,     #list of all student and there info
        'adder': "http://localhost:8000/teacher/addAttendance/?tname="+i_name,
        'dashboard': "http://localhost:8000/teacher/?tname="+i_name,
        'c':coursesList,
        # 'b':        #sheet id      
    }
    # print(context)
    return HttpResponse(template.render(context,request))

def fascript(request):
    # i_name='Nauman Ghazi'

    i_name=request.GET.get('tname', '')
    i_sheetid=request.GET.get('tsheet', '')
    tsheet=int(i_sheetid)

    a=foo()

    stu=a['humannames']
    numofstu=a['no_of_faces']
    # stu = list(map(int, stu))
    ans=a['ans']

    # stu=['Raza Vasnani','Mehdi Raza Rajnai','Ammar Rizwan','Mujtaba Bawani']
    # numofstu=2
    # ans=[2,3]
    nmlist=[]

    CrsTchr_id=AttendanceSheet.objects.filter(sheet_id = tsheet).values_list('crs_tchr_id')
    print(CrsTchr_id) # CrsTchr_id = 9
    Crs_id=CourseTeacher.objects.filter(id = CrsTchr_id[0][0]).values_list('crs_Id')
    print(Crs_id) # Crs_id = 8
    EnrollCourse_id=EnrolledCourse.objects.filter(crs_Id = Crs_id[0][0]).values_list('std_Id')
    print(EnrollCourse_id)
    ll=list(EnrollCourse_id)
    # print(stu)
    
    for i in range(numofstu):
        iname=stu[ans[i]]
        po=Student.objects.filter(fName=iname).values_list('id')[0][0]
        print(po,"**",ll)
        if (po,) in ll: 
            nmlist.append(iname)
            AttendanceSheet.objects.filter(sheet_id=tsheet).values_list('crs_tchr_id')[0]
            att1 = Attendance(attendance_id=1, status="P",std_id=Student.objects.get(fName = iname),AttendSheet_id=AttendanceSheet.objects.get(sheet_id = tsheet))
            att1.pk=None
            att1.save()
            # print(att1)


    #tahir yaha pr absent record bhi enter krna hai

    
    for i in EnrollCourse_id:
        Stu_name = Student.objects.filter(id =i[0]).values_list('fName')
        if Stu_name[0][0] not in nmlist:
            att1=Attendance(attendance_id=1, status="A",std_id=Student.objects.get(fName = Stu_name[0][0]),AttendSheet_id=AttendanceSheet.objects.get(sheet_id = tsheet))
            att1.pk=None
            att1.save()    
    ########################################code

    template=loader.get_template('teacher/signup.html')
    context={
    }
    response = redirect('/teacher/viewsheet/?tname='+i_name+'&tsheet='+i_sheetid)
    return response

def temp(request):
    crs_tchr_id=request.GET.get('crs_tchr_id', '')
    crs_tchr_id=int(crs_tchr_id)
    date=request.GET.get('date', '')

    pp=AttendanceSheet.objects.filter(date=date,crs_tchr_id=crs_tchr_id).values_list('sheet_id')[0][0]
    pp1=CourseTeacher.objects.filter(id=crs_tchr_id).values_list('tchr_id')[0][0]
    pp2=Teacher.objects.filter(id=pp1).values_list('name')[0][0]
    print(pp)
    response = redirect('/teacher/viewsheet/?tname='+pp2+'&tsheet='+str(pp))
    return response

def notification(request):

    template=loader.get_template('teacher/notification.html')
    
    context={
    }
    
    return HttpResponse(template.render(context,request))
