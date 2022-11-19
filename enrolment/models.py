from django.db import models

# DB에 관한 내용들
# 태이블 생성할때마다   python manage.py makemigrations
#                    python manage.py migrate
# 그리고 admin.py에서 admin.site.register(User) 해줘야댐

class Student(models.Model):  # 학생 테이블(PK = 학번)
    studentNumber = models.TextField(primary_key=True)  # 학번
    email = models.EmailField()  # 이메일
    password = models.TextField()  # 비밀번호
    name = models.TextField()  # 이름
    grade = models.IntegerField()  # 학년
    credit = models.IntegerField()  # 현재 수강 학점
    majorName = models.TextField()  # 학과


class Course(models.Model):  # 강의 테이블(PK = 학수번호)
    courseNumber = models.TextField(primary_key=True)  # 학수 번호(과목 번호 + 분반)
    subjectName = models.TextField()  # 과목명
    majorName = models.TextField()  # 학과명
    grade = models.IntegerField()  # 대상 학년
    credit = models.IntegerField()  # 이수 학점
    professorName = models.TextField()  # 교수명
    limitNumber = models.IntegerField()  # 정원
    currentNumber = models.IntegerField()  # 현재 수강 신청 인원


class ApplyCourse(models.Model):  # 수강신청 테이블
    studentNumber = models.ForeignKey(Student, on_delete=models.CASCADE)  # Student table의 PK인 studentNumber
    courseNumber = models.ForeignKey(Course, on_delete=models.CASCADE)  # Course table의 PK인 courseNumber


class Admin(models.Model): # 관리자 테이블
    email = models.EmailField() # 관리자 이메일
    password = models.TextField() # 관리자 비밀번호
