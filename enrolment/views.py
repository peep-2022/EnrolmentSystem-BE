from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ApplyCourse, Course, Admin, Student
from .serializers import CourseSerializer


class showEnrolmentList(APIView):
    def get(self, request):
        _studentNumber = request.query_params.get('studentNumber')

        AC_list = ApplyCourse.objects.filter(studentNumber=_studentNumber)
        print(AC_list)

        result_list = list()
        for item in AC_list:
            CL = Course.objects.filter(courseNumber=item.courseNumber.courseNumber)
            for j in CL:
                course_info = CourseSerializer(j)
                result_list.append(course_info.data)

        if result_list:
            return Response(result_list)

        return Response({
            'returnCode': 'Fail'
        })

class dropClass(APIView):
    def get(self, request):
        _studentNumber = request.query_params.get('studentNumber')
        _courseNumber = request.query_params.get('courseNumber')

        AC = ApplyCourse.objects.filter(studentNumber=_studentNumber, courseNumber=_courseNumber)

        if AC:
            AC.delete()
            return Response({"returnCode": "Success"})
        return Response({"returnCode": "Fail"})

class login(APIView):
    def get(self, request):
        _isStudent = request.query_params.get('isStudent')
        _id = request.query_params.get('id')
        _password = request.query_params.get('password')

        if _isStudent == True:
            for student in Student:
                if student.studentNumber == _id:
                    if student.password == _password:
                        return Response({
                            'isSuccess': 'true'
                        })
        elif _isStudent == False:
            for admin in Admin:
                if admin.email == _id:
                    if admin.password == _password:
                        return Response({
                            'isSuccess': 'true'
                        })

        else:
            return Response({
                'isSuccess': 'fail'
            })