# 방법1
print("나는 %d살입니다" % 20)
print("나는 %s을 좋아합니다" % "파이썬")
print("Apple은 %c로 시작합니다" % "A")
print("나는 %s색과 %s색을 좋아합니다" % ("파란", "빨간"))


# 방법2
print("나는 {}살입니다" .format(20))
print("나는 {}색과 {}색을 좋아합니다" .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아합니다" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아합니다" .format("파란", "빨간"))


# 방법3
print("나는 {age}살이며, {color}색을 좋아합니다" .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아합니다" .format(color = "빨간", age = 20))

# 방법4
age = 20
color = "노란"
print(f"나는 {age}살이며, {color}색을 좋아합니다")