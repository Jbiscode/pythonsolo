결석자 = [2,5]
책X = [8]

for 학생 in range(1,11):
    if 학생 in 결석자:
        continue
    elif 학생 in 책X:
        print("오늘수업 여기까지.{0}번 학생 교무실로".format(학생))
        break
    print("{0}번 일어나서 읽어봐".format(학생))