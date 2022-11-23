import urllib
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course

class AdminUpdate(APIView):
    def get(self, request):
        # 요청변수값 변수에 저장
        _oldCourseNumber = urllib.parse.unquote(request.query_params.get('oldCourseNum'))
        _newCourseNumber = urllib.parse.unquote(request.query_params.get('newCourseNum'))
        _subjectName = urllib.parse.unquote(request.query_params.get('subjectName'))
        _limitNumber = request.query_params.get('limitNumber')
        _grade = request.query_params.get('grade')
        _credit = request.query_params.get('credit')
        _professorName = urllib.parse.unquote(request.query_params.get('professorName'))
        _majorName = urllib.parse.unquote(request.query_params.get('majorName'))

        # 기존 학수번호와 변경하고자 하는 학수번호가 동일한지 확인
        if _oldCourseNumber != _newCourseNumber:
            for c in Course.objects.all():
                if c.courseNumber == _newCourseNumber: #이미 존재하는 학수번호로 변경을 시도할 때
                    return Response({
                        'returnCode': 'OverlappedError' #중복 에러
                    })

            #존재하지 않는 학수번호로 변경을 시도할 때
            course = Course.objects.get(courseNumber=_oldCourseNumber) #학수번호로 수정이 필요한 튜플을 가져옴
            course.courseNumber = _newCourseNumber
            course.subjectName = _subjectName
            course.limitNumber = _limitNumber
            course.grade = _grade
            course.credit = _credit
            course.professorName = _professorName
            course.majorName = _majorName
            course.save() #수정된 새로운 튜플이 저장됨
            Course.objects.get(courseNumber=_oldCourseNumber).delete() #기존 튜플 제거
            return Response({
                'returnCode': 'Success' #수정 성공
            })

        else: #학수번호 동일, 다른 항목 변경할 때
            isChange = False
            course = Course.objects.get(courseNumber= _oldCourseNumber)
            # Course 테이블에서 _courseNumber와 같은 값을 가진 튜플 가져옴

            if course.subjectName != _subjectName:
                course.subjectName = _subjectName
                isChange = True
            if course.limitNumber != _limitNumber:
                course.limitNumber = _limitNumber
                isChange = True
            if course.grade != _grade:
                course.grade = _grade
                isChange = True
            if course.credit != _credit:
                course.credit = _credit
                isChange = True
            if course.professorName != _professorName:
                course.professorName = _professorName
                isChange = True
            if course.majorName != _majorName:
                course.majorName = _majorName
                isChange = True

            course.save() #수정된 튜플 저장

            if isChange == False:
                return Response({ #아무것도 변경되지 않음
                    'returnCode': 'NoChangeError'
                })
            else:
                return Response({ #수정 성공
                    'returnCode': 'Success'
                })

        return Response({ #기타 오류
                'returnCode': 'Fail'
            })

