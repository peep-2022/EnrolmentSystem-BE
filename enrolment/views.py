from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import User

# Create your views here.

class infolist(APIView):
    def get(self, request):
        # DB에 접근하는 코드
        # 요청변수를 추출하여 변수에 저장
        id = request.query_params.get('userid')

        user = User.objects.get(userid=id)

        return Response({
            "d":user.userid
        })

    # setting에 restframework 넣어주어야함