from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import Course


# Create your views here.

class searchList(APIView):
    def get(self, request):
        # DB에 접근하는 코드
        # 요청변수를 추출하여 변수에 저장
        _majorName = request.query_params.get('majorName')
        _grade = request.query_params.get('grade')
        _credit = request.query_params.get('credit')
        _professorName = request.query_params.get('professorName')
        _subjectName = request.query_params.get('subjectName')
        _courseNumber = request.query_params.get('courseNumber')
        _classNumber = request.query_params.get('classNumber')
        _currentNumber = request.query_params.get('currentNumber')
        _limitNumber = request.query_params.get('limitNumber')

        if _majorName == '대학 학과공통':
            cls = Course.objects.filter(grade=_grade, credit=_credit, subjectName=_subjectName,
                                        courseNumber=_courseNumber, professorName=_professorName,
                                        limitNumber=_limitNumber, currentNumber=_currentNumber).values()
        else:
            cls = Course.objects.filter(majorName=_majorName, grade=_grade, credit=_credit, subjectName=_subjectName,
                                        courseNumber=_courseNumber, professorName=_professorName,
                                        limitNumber=_limitNumber, currentNumber=_currentNumber).values()

        return_list = list()
        for item in return_list :
            return_list.append(item)

        if return_list :
            return Response(cls)
        return Response({
            'returnCode' : 'NoneError'
        })


    # setting에 restframework 넣어주어야함
