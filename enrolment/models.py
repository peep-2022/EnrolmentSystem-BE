from django.db import models

from django.db import models

class Student(models.Model): #학생 테이블(PK = 학번)
    studentNumber = models.TextField(primary_key=True) #학번
    email = models.EmailField() #이메일
    password = models.TextField() #비밀번호
    name = models.TextField() #이름
    grade = models.IntegerField() #학년
    credit = models.IntegerField() #현재 수강 학점
    majorName = models.TextField() #학과

# class Course(models.Model): #강의 테이블(PK = 과목번호, 분반)
#     subjectNumber = models.TextField(primary_key=True) #과목 번호
#     classNumber = models.TextField(primary_key=True) #분반
#     subjectName = models.TextField() #과목명
#     majorName = models.TextField() #학과명
#     grade = models.IntegerField() #대상 학년
#     credit = models.IntegerField() #이수 학점
#     professorName = models.TextField() #교수명
#     limitNumber = models.IntegerField() #정원
#     currentNumber = models.IntegerField() #현재 수강 신청 인원
#
# class ApplyCourse(models.Model):
#     studentNumber = models.ForeignKey(Student)
#     subjectNumber = models.ForeignKey(Course)
#     classNumber = models.ForeignKey(Course)
#
# class Admin(models.Model):
#     adminEmail = models.EmailField()
#     adminPassword = models.TextField()

