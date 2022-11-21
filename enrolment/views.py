from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ApplyCourse, Course, Admin, Student
from .serializers import CourseSerializer
import os
import django

#http://127.0.0.1:8000/enrolment?studentNumber=201801858&courseNumber=1213-3016-01
class enrolment(APIView):
    def get(self, request):
        _studentNumber = request.query_params.get('studentNumber') # 받아온 studentNumber
        _courseNumber = request.query_params.get('courseNumber') # 받아온 courseNumber
        _student = Student.objects.filter(studentNumber=_studentNumber).first() # student 객체
        seleted_course = Course.objects.filter(courseNumber=_courseNumber).first()

        if not _student :
            return Response({
                'returnCode': 'NoneStudentNumberError'
            })

        if not seleted_course :
            return Response({
                'returnCode': 'NoneCourseNumberError'
            })
        # 수강신청 가능 시간 확인 -> 추가필요

        # 이미 수강신청 했는지 확인
        students_enrolmented_course = ApplyCourse.objects.filter(studentNumber=_studentNumber)

        # 수강신청된 course들은 따로따로 applyCourse에 들어가있음
        if students_enrolmented_course: # 학번의 수강신청 데이터가 있는지 확인
            for course_list_item in students_enrolmented_course : # 있으면 돌면서 해당 학수번호의 수강신청 데이터가 있는지 확인
                if course_list_item.courseNumber.courseNumber.find(_courseNumber) > -1: # 있으면 AlreadyAppliedError
                    return Response({
                        'returnCode': 'AlreadyAppliedError'
                    })

                # 같은 강의의 다른 분반을 이미 수강중
                print(course_list_item.courseNumber.courseNumber[:-3])
                if course_list_item.courseNumber.courseNumber[:-3].find(_courseNumber[:-3]) > -1: # 있으면 AlreadyAppliedError
                    return Response({
                        'returnCode': 'AlreadyAppliedSubjectError'
                    })

        # 정원 초과인지 확인
        _limitNumber = seleted_course.limitNumber
        _currentNumber = seleted_course.currentNumber
        if (_limitNumber - _currentNumber) < 1:
            return Response({
                'returnCode': 'OverlimitError'
            })

        # 들을 수 있는 학점 초과했는지 확인

        if (_student.credit + seleted_course.credit) > 9:
            return Response({
                'returnCode': 'OvercreditError'
            })

        before_credit = _student.credit

        try:
            _student.credit = _student.credit + seleted_course.credit
            _student.save()
            print("credit 덧셈 완료")
            ApplyCourse.objects.create(studentNumber=_student, courseNumber=seleted_course)
            print("apply_course 생성 완료")
            return Response({
                'returnCode': 'Success'
            })
        except:
            if before_credit != _student.credit :
                print("credit 원래대로 복구")
                _student.credit = before_credit
            return Response({
                'returnCode': 'OverlapError'
            })


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

class adminDelete(APIView):
    def delete(self, request):
        _courseNumber = request.query_params.get('courseNumber')

        course = Course.objects.get(courseNumber=_courseNumber)
        course.delete()

        if course:
            return Response({
                'returnCode': 'Success'
            })

        return Response({
                'returnCode': 'Fail'
            })

class login(APIView):
    def get(self, request):
        _isStudent = request.query_params.get('isStudent')
        _id = request.query_params.get('id')
        _password = request.query_params.get('password')

        answer = False
        if _isStudent == 'true':
            for student in Student.objects.all():
                if student.studentNumber == _id:
                    if student.password == _password:
                        answer = True

        elif _isStudent == 'false':
            for admin in Admin.objects.all():
                if admin.email == _id:
                    if admin.password == _password:
                        answer = True

        if answer == True:
            return Response({
                'isSuccess': 'true'
            })
        else:
            return Response({
                'isSuccess': 'fail'
            })
