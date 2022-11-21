import urllib
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course

class AdminUpdate(APIView):
    def get(self, request):
        _oldCourseNumber = request.query_params.get('oldCourseNum')
        _newCourseNumber = request.query_params.get('newCourseNum')
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
            old_course = Course.objects.get(courseNumber=_oldCourseNumber)
            old_course.delete() #기존 컬럼 삭제
            new_course = Course(courseNumber = _newCourseNumber, subjectName = _subjectName, limitNumber=_limitNumber, grade=_grade, credit=_credit, professorName=_professorName, majorName=_majorName)
            new_course.save() #새로운 학수번호로 새 컬럼 생성
            return Response({
                'returnCode': 'Success'
            })

        else: #학수번호 동일, 다른 항목 변경
            isChange = False
            course = Course.objects.get(courseNumber= _newCourseNumber)
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

