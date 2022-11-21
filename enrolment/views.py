import urllib
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course

class AdminUpdate(APIView):
    def get(self, request):
        _oldCourseNumber = urllib.parse.unquote(request.query_params.get('oldCourseNum'))
        _newCourseNumber = urllib.parse.unquote(request.query_params.get('newCourseNum'))
        _subjectName = urllib.parse.unquote(request.query_params.get('subjectName'))
        _limitNumber = request.query_params.get('limitNumber')
        _grade = request.query_params.get('grade')
        _credit = request.query_params.get('credit')
        _professorName = urllib.parse.unquote(request.query_params.get('professorName'))
        _majorName = urllib.parse.unquote(request.query_params.get('majorName'))
        # 요청변수값 변수에 저장

        # 변경하고자 하는 학수번호와 동일한지 확인
        if _oldCourseNumber != _newCourseNumber: #학수번호 변경
            for c in Course.objects.all():
                if c.courseNumber == _newCourseNumber: #이미 존재하는 학수번호로 변경을 시도할 때
                    return Response({
                        'returnCode': 'OverlappedError'
                    })
            #존재하지 않던 학수번호로 변경 시도
            course = Course.objects.get(courseNumber=_oldCourseNumber)
            course.courseNumber = _newCourseNumber
            course.subjectName = _subjectName
            course.limitNumber = _limitNumber
            course.grade = _grade
            course.credit = _credit
            course.professorName = _professorName
            course.majorName = _majorName
            course.save()
            Course.objects.get(courseNumber=_oldCourseNumber).delete()
            return Response({
                'returnCode': 'Success'
            })

        else: #학수번호 동일, 다른 항목 변경
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

            course.save()

            if isChange == False:
                return Response({ #아무것도 변경되지 않음
                    'returnCode': 'NoChangeError'
                })
            else:
                return Response({
                    'returnCode': 'Success'
                })

        return Response({
                'returnCode': 'Fail'
            })

