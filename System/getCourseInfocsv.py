import pandas as pd
import numpy as np

arr1 = np.array([['개설학과', '대상학년', '과목번호', '분반', '과목명', '정원', '수강인원', '학점/시수', "담당교수"]])


f = open("courseInfo.txt", 'r', encoding='UTF-8')
lines = f.readlines()
for line in lines:
    temp = line.split('aria-label="')
    temp_ary = []
    for i in temp :
        # print(i)
        temp_str = i.split('"')
        # print(temp_str)
        if((temp_str[0].find("div")!=-1) | (temp_str[0].find("행 번호")!=-1)):
            continue
        make_data = temp_str[0].split(" ", 2)
        if (len(make_data) < 2) :
            continue
        if (((make_data[1].find("9열") != -1) or (make_data[1].find("11열") != -1)) or (make_data[1].find("12열") != -1)):
            # print(temp_ary)
            # print("예외처리")
            continue
        # print(make_data)

        if (make_data[1].find("5열") != -1):
            temp_data = i.split("</div></a>")
            # print("temp_data임 ", temp_data)
            if (len(temp_data) > 1):
                temp_str_ary = temp_data[0].split(">")
                # print(temp_str_ary[-1] + "를 추가할거임")
                temp_ary += [make_data[2]]
                temp_ary += [temp_str_ary[-1]]
                continue

        if (make_data[1].find("6열") != -1):
            temp_data = i.split("</div></a>")
            if (len(temp_data) > 1):
                temp_str_ary = temp_data[0].split(">")
                # print(temp_str_ary[-1] + "를 추가할거")
                temp_ary += [temp_str_ary[-1]]
                continue
        if (make_data[1].find("10열") != -1):
            temp_data = i.split("/")
            if (len(temp_data) > 2):
                # print(temp_data[0][-1] + "를 추가할거")
                temp_ary += [temp_data[0][-1]]
                continue
        if(len(make_data) <= 3) :
            if (len(make_data) <= 2) :
                continue
            elif(make_data[2] == ''):
                continue
            else :
                temp_ary += [make_data[2]]
        else :
            temp_ary += [make_data[2]]

        if len(temp_ary) == 9 :
            print(temp_ary)

        if(make_data[1].find("13열")!=-1):
            if(len(temp_ary) != 9) :
                print("!!!!!!!!!!", temp_ary)
            arr2 = np.array([temp_ary])
            temp_ary = []
            arr1 = np.concatenate((arr1, arr2), axis=0)
        if (make_data[1].find("31열") != -1):
            temp_ary = []
        # if len(temp_ary)
df = pd.DataFrame(arr1)
df.to_csv('courseInfo.csv', index=False, encoding='cp949')
f.close()