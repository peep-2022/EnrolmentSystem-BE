from django.urls import path
from django.conf import settings
from .views import infolist

urlpatterns = [
    path('yejin', infolist.as_view(), name='yejin'),
]