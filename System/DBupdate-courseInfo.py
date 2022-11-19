import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EnrolmentSystemPrj.settings')
django.setup()

from enrolment.models import Course

with open('courseInfo.csv') as csv_file:
    rows = csv.reader(csv_file)
    next(rows, None)
    next(rows, None)

    for row in rows:
        classNumber = ''
        if len(row[3]) == 1: #분반이 한글자이면 0을 붙임 예) 03
            classNumber = '0' + row[3]
        else:
            classNumber = row[3]

        try:
            Course.objects.create(
                courseNumber=row[2] + '-' + classNumber,
                subjectName=row[4],
                majorName=row[0],
                grade=row[1],
                credit=row[7],
                professorName=row[8],
                limitNumber=row[5],
                currentNumber=0
            )
        except:
            print("중복 처리")
