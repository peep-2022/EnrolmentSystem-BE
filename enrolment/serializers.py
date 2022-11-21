from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('courseNumber', 'subjectName', 'majorName', 'grade', 'credit', 'professorName', 'limitNumber', 'currentNumber')
