# 문자열을 역순으로 출력하는 함수
def print_reverse(str) :
    print(str[::-1])

print_reverse("python")



# 리스트를 입력 받아 평균을 출력
def print_score(list) :
    print(sum(list) / len(list))

print_score([1,2,3])



# dictionary 키 값을 받아 리스트를 출력
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dict, key) :
    print(dict[key])

print_value_by_key(my_dict, "10/26")



# 입력된 글자 수만큼 출력하는 함수
def print_mxn(str, cnt) :
    i = 0
    while i < len(str) :
        print(str[i:cnt + i])
        i = i + cnt

print_mxn("아이엠어보이유알어걸", 3)


# return 사용
def calc_monthly_salary(salary) :
    result = int(salary / 12) # 1원 미만은 절사
    return result

salary = calc_monthly_salary(12000000)
print(salary)



# 변수에 값을 바인딩
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200) # a변수에는 200을 b변수에는 100을 바인딩


# 문자열을 입력받아 리스트로 반환
def make_list(string) :
    list_str = []
    for str in string :
        list_str.append(str)
    return list_str

print(make_list("abcd"))


# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 함수
def convert_int(num) :
    return int(num.replace(",", ""))

print(convert_int("1,234,567"))

