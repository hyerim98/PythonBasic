jumin = "990129-1234567"

print("성별 : " + jumin[7])
# 0 부터 2 직전까지(0 ~ 1번째 값을 가져옴)
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

# 처음부터 6 직전까지
print("생년월일 : " + jumin[:6])
# 7 부터 끝까지
print("뒤 7자리 : " + jumin[7:])
# -7번째 : 1, -1번째 : 7
print("뒤 7자리(뒤에 부터) : " + jumin[-7:])