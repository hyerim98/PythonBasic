# file을 쓰기 목적으로 생성
score_file = open("score.txt", "w", encoding="utf8")
print("math : 0", file=score_file)
print("eng : 50", file=score_file)
score_file.close()

# file을 이어쓰기 목적으로 열기
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("science : 80")
score_file.write("\ncoding : 100")
score_file.close()

# file을 읽는 목적으로 열기
score_file = open("score.txt", "r", encoding="utf8")
# read : 모든 내용 읽기
# readline : 한 줄 읽기
print(score_file.read())
score_file.close()

# file 내용 한 줄씩 읽기
score_file = open("score.txt", "r", encoding="utf8")
while True :
    line = score_file.readline()
    if not line :
        break
    print(line)
score_file.close()

# file 내용을 한 줄씩 리스트 형태로 저장
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines :
    print(line, end = "")
score_file.close()