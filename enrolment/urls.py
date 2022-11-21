from django.contrib import admin
from django.urls import path
from enrolment.views import AdminUpdate

urlpatterns = [
    path('adminUpdate/', AdminUpdate.as_view())
]