from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course

class AdminUpdate(APIView):
    def get(self, request):
        _courseNumber = request.query_params.get('courseNumber')
        _subjectName = request.query_params.get('subjectName')
        _limitNumber = request.query_params.get('limitNumber')
        _grade = request.query_params.get('grade')
        _credit = request.query_params.get('credit')
        _professorName = request.query_params.get('professorName')
        _majorName = request.query_params.get('majorName')
        # 요청변수값 변수에 저장

        # 변경하고자 하는 학수번호와 동일한지 확인
        for c in Course.objects.all():
            if c.courseNumber == _courseNumber:
                return Response({
                    'returnCode': 'OverlappedError'
                })

        course = Course.objects.get(courseNumber= _courseNumber)
        # Course 테이블에서 _courseNumber와 같은 값을 가진 튜플 가져옴

        course.subjectName = _subjectName
        course.limitNumber = _limitNumber
        course.grade = _grade
        course.credit = _credit
        course.professorName = _professorName
        course.majorName = _majorName
        course.save()

        if course:
            return Response({
                'returnCode': 'Success'
            })

        return Response({
                'returnCode': 'Fail'
            })

