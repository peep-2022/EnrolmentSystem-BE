from django.db import models

from django.db import models

class Student(models.Model):
    studentNumber = models.TextField(primary_key=True) #학번
    studentEmail = models.EmailField() #이메일
    studentPassword = models.TextField() #비밀번호
    studentName = models.TextField() #이름
    studenGrade = models.IntegerField() #학년
    studentCredit = models.IntegerField() #현재 수강 학점
    studentMajorName = models.TextField() #학과

# class Course(models.Model):
#     subjectNumber = models.TextField(primary_key=True)
#     classNumber = models.TextField(primary_key=True)
#     subjectName = models.TextField()
#     majorName = models.TextField()
#     grade = models.IntegerField()
#     credit = models.IntegerField()
#     limitNumber = models.IntegerField()
#     professorName = models.TextField()
#     currentNumber = models.IntegerField()
#
# class ApplyCourse(models.Model):
#     studentNumber = models.ForeignKey(Student)
#     subjectNumber = models.ForeignKey(Course)
#     classNumber = models.ForeignKey(Course)
#
# class Admin(models.Model):
#     adminEmail = models.EmailField()
#     adminPassword = models.TextField()

