from django.urls import include, path
from rest_framework import routers
from webapp import views

router = routers.DefaultRouter()
router.register('student', views.StudentList)
router.register('institute', views.InstituteList)
router.register('course', views.CourseList)
router.register('teacher', views.TeacherList)
router.register('attendancesheet', views.AttendanceSheetList)
router.register('attendance', views.AttendanceList)
router.register('enrolledcourse', views.EnrolledCourseList)
router.register('courseteacher', views.CourseTeacherList)


#router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('' , include(router.urls)),
]