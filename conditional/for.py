for waiting_no in [0, 1, 2, 3, 4] : # == range(5), range(0, 5)
    print("대기번호 : {0}" .format(waiting_no))


starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks :
    print("{0}, 커피가 준비되었습니다" .format(customer))



# 한 줄 for문
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [i.upper() for i in students]
print(students)
students = [len(i) for i in students]
print(students)
