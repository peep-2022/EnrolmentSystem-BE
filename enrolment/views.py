from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ApplyCourse, Course, Admin, Student
from .serializers import CourseSerializer
from .serializers import CourseSerializer
from django.shortcuts import render
from .models import ApplyCourse, Course, Admin, Student
import urllib

# changeEnrolmentTime에 사용
from datetime import datetime
from System.EnrolmentTime import setSysStartTime, setSysEndTime, sysStartTime, sysEndTime
import time
import urllib


class changeEnrolmentTime(APIView):

    def get(self, request):
        _startTime = request.query_params.get('startTime')
        _endTime = request.query_params.get('endTime')
        _startTimeStamp = time.mktime(datetime.strptime(_startTime, '%Y-%m-%d %H:%M:%S').timetuple())
        _endTimeStamp = time.mktime(datetime.strptime(_endTime, '%Y-%m-%d %H:%M:%S').timetuple())
        
        urllib.parse.unquote(_startTime)
        urllib.parse.unquote(_endTime)
        # 현재 시간
        todaytimestamp = time.time()
        if _endTimeStamp - todaytimestamp < 0 : # 끝나는 시간이 현재 시간보다 이전인경우
            return Response({
                'returnCode': 'EndTimeError'
            })
        if _endTimeStamp - _startTimeStamp < 0 : # 끝나는 시간이 시작시간보다 이전인경우
            return Response({
                'returnCode': 'TimeRangeError'
            })
        try: # 성공
            setSysStartTime(datetime.fromtimestamp(_startTimeStamp))
            setSysEndTime(datetime.fromtimestamp(_endTimeStamp))
            return Response({
                'returnCode': 'Success'
            })
        except: #실패
            return Response({
                'returnCode': 'Fail'
            })

class searchList(APIView):
    def get(self, request):
        _majorName = request.query_params.get('majorName')
        _grade = request.query_params.get('grade')
        _professorName = request.query_params.get('professorName')
        _subjectName = request.query_params.get('subjectName')
        _courseNumber = request.query_params.get('courseNumber')

        urllib.parse.unquote(_subjectName)
        urllib.parse.unquote(_majorName)
        urllib.parse.unquote(_professorName)

        # 선택한 학과가 있는 경우 filter
        if _majorName.find('대학 학과공통') > -1 :
            cls = Course.objects.all()
        else :
            cls = Course.objects.filter(majorName=_majorName)

        try :
            # courseNumber가 있을경우 filter
            if _courseNumber != 'None':
                cls = cls.filter(courseNumber=_courseNumber)

            # grade가 있을경우 filter
            if _grade != '0' :
                cls = cls.filter(grade=_grade)

            # professorName가 있을경우 filter 해당 문자열으로 시작하는 값 / 끝나는 값 / 포함하는 값을 모두 포함하게 검색
            if _professorName != 'None':
                cls = cls.filter(professorName__istartswith=_professorName) \
                      | cls.filter(professorName__iendswith=_professorName) \
                      | cls.filter(professorName__icontains=_professorName)

            # currentNumber가 있을경우 filter 해당 문자열으로 시작하는 값 / 끝나는 값 / 포함하는 값을 모두 포함하게 검색
            if _subjectName != 'None':
                cls = cls.filter(subjectName__istartswith=_subjectName) \
                      | cls.filter(subjectName__iendswith=_subjectName) \
                      | cls.filter(subjectName__icontains=_subjectName)

            if cls : # 필터링된 value가 있는경우 response해준다
                return Response(cls.values())

            else :
                return Response({
                    'returnCode': 'NoneError'
                })
        except:
            return Response({
                'returnCode': 'Error'
            })

class enrolment(APIView):
    def get(self, request):
        _studentNumber = request.query_params.get('studentNumber')  # 받아온 studentNumber
        _courseNumber = request.query_params.get('courseNumber')  # 받아온 courseNumber
        _student = Student.objects.filter(studentNumber=_studentNumber).first()  # student 객체
        seleted_course = Course.objects.filter(courseNumber=_courseNumber).first()

        if not _student:
            return Response({
                'returnCode': 'NoneStudentNumberError'
            })

        if not seleted_course:
            return Response({
                'returnCode': 'NoneCourseNumberError'
            })

        # 수강신청 가능 시간 확인
        _startTimeStamp = sysStartTime()
        _endTimeStamp = sysEndTime()
        sysStartTimeStamp = time.mktime(_startTimeStamp.timetuple())
        sysEndTimeStamp = time.mktime(_endTimeStamp.timetuple())

        todaytimestamp = time.time()
        if (todaytimestamp - sysStartTimeStamp < 0) | (sysEndTimeStamp - todaytimestamp < 0) :
            return Response({
                'returnCode': 'TimeError'
            })

        # 이미 수강신청 했는지 확인
        students_enrolmented_course = ApplyCourse.objects.filter(studentNumber=_studentNumber)

        # 수강신청된 course들은 따로따로 applyCourse에 들어가있음
        if students_enrolmented_course:  # 학번의 수강신청 데이터가 있는지 확인
            for course_list_item in students_enrolmented_course:  # 있으면 돌면서 해당 학수번호의 수강신청 데이터가 있는지 확인
                if course_list_item.courseNumber.courseNumber.find(_courseNumber) > -1:  # 있으면 AlreadyAppliedError
                    return Response({
                        'returnCode': 'AlreadyAppliedError'
                    })

                # 같은 강의의 다른 분반을 이미 수강중
                print(course_list_item.courseNumber.courseNumber[:-3])
                if course_list_item.courseNumber.courseNumber[:-3].find(
                        _courseNumber[:-3]) > -1:  # 있으면 AlreadyAppliedError
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
            # 학생데이터의 수강학점을 추가해주고 수강신청디비에 object 추가
            _student.credit = _student.credit + seleted_course.credit
            _student.save()
            ApplyCourse.objects.create(studentNumber=_student, courseNumber=seleted_course)
            return Response({
                'returnCode': 'Success'
            })
        except:
            # credit 원래대로 복구
            if before_credit != _student.credit:
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
    def delete(self, request):
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
