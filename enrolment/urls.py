from django.urls import path
from django.conf import settings
from .views import showEnrolmentList, dropClass

urlpatterns = [
    path('showEnrolmentList', showEnrolmentList.as_view(), name='showEnrolmentList'),
    path('dropClass', dropClass.as_view(), name='dropClass'),
]