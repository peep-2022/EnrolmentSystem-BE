from django.db import models

# Create your models here.
# DB에 관한 내용들
# 태이블 생성할때마다   python manage.py makemigrations
#                    python manage.py migrate
# 그리고 admin.py에서 admin.site.register(User) 해줘야댐

class Class(models.Model):
    # 컬럼명 = 타입()
    majorName = models.TextField(default='대학 학과공통')
    grade = models.TextField(default='')
    credit = models.TextField(default='')
    subjectName = models.TextField(default='')
    subjectNumber = models.TextField(default='')
    classNumber = models.TextField(default='')
    professorName = models.TextField(default='')
    limitNumber = models.TextField(default='0')
    currentNumber = models.TextField(default='')
