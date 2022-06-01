'''
    보고서 형식

    - X주차 주간보고 -
    부서 : 
    이름 : 
    업무 요약 : 

    1주차 ~ 5주차까지 생성

    파일명 : 1주차.txt, 2주차.txt , ....
'''

for i in range(1, 6) :
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file :
        report_file.write("- {0}주차 주간보고 - ".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")

