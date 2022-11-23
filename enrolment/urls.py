from django.urls import path
from django.conf import settings
from .views import showEnrolmentList, dropClass, adminDelete, login, enrolment, searchList, AdminUpdate

urlpatterns = [
    path('showEnrolmentList', showEnrolmentList.as_view(), name='showEnrolmentList'),
    path('dropClass', dropClass.as_view(), name='dropClass'),
    path('adminDelete', adminDelete.as_view(), name='adminDelete'),
    path('login', login.as_view(), name='login'),
    path('enrolment', enrolment.as_view(), name='enrolment'),
    path('search', searchList.as_view(), name='Class'),
    path('adminUpdate', AdminUpdate.as_view(), name="adminUpdate")
]
