'''
    * continue : 해당되는거 제외하고 실행됨
    * break : 반복문 종료
'''

absent = [2, 5]
no_book = [7]

for student in range(1, 11) :
    if student in absent : # student가 absent에 속해있나를 확인하는 작업
        continue
    elif student in no_book :
        print("오늘 수업 끝. {0}번은 따라오세요" .format(student))
        break

    print("{0}, 책 읽어봐".format(student))