from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

class infolist(APIView):
    def get(self, request):

        #db 접근하는 코드
        id = request.query_params.get('userid')
        pw = request.query_params.get('userpw')
        user = User.objects.get(userid=id)

        return Response({
            'good'
        })