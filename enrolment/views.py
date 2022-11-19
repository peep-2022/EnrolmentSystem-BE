from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import Class

# Create your views here.

class searchList(APIView):
    def get(self, request):
        # DB에 접근하는 코드
        # 요청변수를 추출하여 변수에 저장
        _majorName = request.query_params.get('majorName')
        _grade = request.query_params.get('grade')
        _professorName = request.query_params.get('professorName')
        _subjectName = request.query_params.get('subjectName')
        _subjectNumber = request.query_params.get('subjectNumber')
        _classNumber = request.query_params.get('classNumber')

        if _majorName == '대학 학과공통' :
            print("대학학과공통")
            cls = Class.objects.filter(grade=_grade, professorName=_professorName,
                                    subjectName=_subjectName, subjectNumber=_subjectNumber, classNumber=_classNumber).values()
        else :
            cls = Class.objects.filter(majorName=_majorName, grade=_grade, professorName=_professorName,
            subjectName=_subjectName, subjectNumber=_subjectNumber, classNumber=_classNumber).values()

        print(cls)

        return Response({
            cls
            # 'majorName': cls.majorName,
            # 'grade': cls.grade,
            # 'credit': cls.credit,
            # 'subjectName': cls.subjectName,
            # 'subjectNumber': cls.subjectNumber,
            # 'classNumber': cls.classNumber,
            # 'professorName': cls.professorName,
            # 'limitNumber': cls.limitNumber,
            # 'currentNumber': cls.currentNumber
        })

    # setting에 restframework 넣어주어야함