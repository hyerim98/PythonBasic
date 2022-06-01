# sep
print("Python", "Java", "JavaScript", sep=" vs ")

# end
print("Python", "Java", sep = ",", end = "?")
print("Java")

import sys
# stdout : 표준출력으로 처리
# stderr : 표준에러로 처리
print("Python", "Java", file = sys.stdout)
print("Python", "Java", file = sys.stderr)


# dictionary 출력
scores = {"math" : 0, "eng" : 50, "coding" : 100}
for subject, score in scores.items() :
    # ljust : 8칸 공간을 확보한 왼쪽 정렬
    # rjust : 4칸 공간을 확보한 오른쪽 정렬
    print(subject.ljust(8), str(score).rjust(4), sep = ":") 


# zfill : 0 채워서 출력
for num in range(1, 21) :
    print("대기번호 : " + str(num).zfill(3)) # 3자리 출력에서 값이 없는 부분은 0으로 채우기

