# 파일 쓰기(with 사용)

# with open("매수종목1.txt", "w", encoding="utf8") as txt_file :
#     txt_file.write("005930 삼성전자\n")
#     txt_file.write("005380 현대차\n")
#     txt_file.write("035420 네이버")

# 엑셀 파일 쓰기
# import csv

# with open("매수종목2.csv", "wt", encoding="cp949", newline='') as txt_file :
#     txt_file = csv.writer(txt_file) # 엑셀파일로 저장
#     txt_file.writerow(["종목명", "종목코드", "PER"])
#     txt_file.writerow(["삼성전자", "005930", "15.79"])
#     txt_file.writerow(["네이버", "035420", "55.82"])


# 파일 읽기
dict = {}

txtFile = open("매수종목1.txt", "r", encoding="utf8")
while True :
    line = txtFile.readline()
    if not line :
        break
    line = line.split(' ')
    dict[line[0]] = line[1].strip() # strip : /n제거
txtFile.close()

print(dict)