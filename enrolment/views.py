from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import Course
import urllib


# Create your views here.

class searchList(APIView):
    def get(self, request):
        # DB에 접근하는 코드
        # 요청변수를 추출하여 변수에 저장

        _majorName = request.query_params.get('majorName')
        _grade = request.query_params.get('grade')
        _professorName = request.query_params.get('professorName')
        _subjectName = request.query_params.get('subjectName')
        _courseNumber = request.query_params.get('courseNumber')

        urllib.parse.unquote(_subjectName)
        urllib.parse.unquote(_majorName)
        urllib.parse.unquote(_professorName)

        if _majorName.find('대학 학과공통') > -1 :
            cls = Course.objects.all()
        else :
            cls = Course.objects.filter(majorName=_majorName)
        print(cls.count())
        # courseNumber가 있을경우 filter
        try :
            if _courseNumber != 'None':
                print("courseNumber not None")
                cls = cls.filter(courseNumber=_courseNumber)
            print(cls.count())

            # grade가 있을경우 filter
            if _grade != '0' :
                print("grade None")
                cls = cls.filter(grade=_grade)
            print(cls.count())
            # professorName가 있을경우 filter 해당 문자열으로 시작하는 값 / 끝나는 값 / 포함하는 값을 모두 포함하게 검색
            if _professorName != 'None':
                print("professorName not None")
                cls = cls.filter(professorName__istartswith=_professorName) \
                      | cls.filter(professorName__iendswith=_professorName) \
                      | cls.filter(professorName__icontains=_professorName)
            print(cls.count())
            # currentNumber가 있을경우 filter
            if _subjectName != 'None':
                print("subjectName not None")
                cls = cls.filter(subjectName__istartswith=_subjectName) \
                      | cls.filter(subjectName__iendswith=_subjectName) \
                      | cls.filter(subjectName__icontains=_subjectName)
            print(cls.count())
            if cls : # 필터링된 value가 있는경우 response해준다
                print("return response")
                return Response(cls.values())

            return Response(cls)
        except:
            return Response({
                'returnCode': 'NoneError'
            })



    # setting에 restframework 넣어주어야함
