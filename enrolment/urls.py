from django.urls import path
from django.conf import settings
from .views import showEnrolmentList, dropClass, adminDelete, login, enrolment, searchList, changeEnrolmentTime

urlpatterns = [
    path('showEnrolmentList', showEnrolmentList.as_view(), name='showEnrolmentList'),
    path('dropClass', dropClass.as_view(), name='dropClass'),
    path('adminDelete', adminDelete.as_view(), name='adminDelete'),
    path('login', login.as_view(), name='login'),
    path('enrolment', enrolment.as_view(), name='enrolment'),
    path('changeEnrolmentTime', changeEnrolmentTime.as_view(), name='changeEnrolmentTime')
    path('search', searchList.as_view(), name='Class')
]
