customer = "토르"
index = 5

while index >= 1 :
    print("{0}, 커피가 준비되었습니다. {1}번 남았습니다." .format(customer, index))

    index -= 1
    if index == 0 :
        print("커피는 폐기처분 되었습니다")


customer = "아이언맨"
person = "Unknown"

while customer != person :
    print("{0}, 커피가 준비되었습니다" .format(customer))
    person = input("이름이 어떻게 되시나요? ")

    index += 1