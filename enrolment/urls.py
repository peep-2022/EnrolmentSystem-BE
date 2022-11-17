from django.urls import path
from django.conf import settings
from enrolment.views import infolist

urlpatterns = [
    path('jiwon/', infolist.as_view(), name='jiwon')
    # path('', Jiwon.as_view(), name='home')
]
## 지원에 들어오면 어떤 함수로 매핑해준다. url이랑 매핑되는 함수를 수행할 수 있는 파일로 간다.
## 그게 views.py인것