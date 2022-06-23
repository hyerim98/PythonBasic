# 환율
환율 = {'달러':1167, '엔':1.096, '유로':1268, '위안':171}
user = input('입력 : ')
money, currency = user.split(" ")
result = float(환율[currency]) * int(money)
print('{}원'.format(result))


# 가장 큰 숫자 출력
nums = []
for i in range(3) :
    nums.append(input('num : '))
print("가장 큰 수 : ", max(nums))


# 통신사
tel_info = {'011':'SKT', '016':'KT', '019':'LGU+', '010':'알수없음'}
tel = input('번호 : ')
tel = tel[0:3]
if tel in tel_info.keys() :
    print('당신은 {} 사용자입니다'.format(tel_info[tel]))


# 우편번호
kangbuk = [0, 1, 2]
dobong = [3, 4, 5]
noone = [6, 7, 8, 9]
postNum = input('우편번호 : ')
postNum1, postNum2 = postNum[0:2], int(postNum[2])

if postNum1 == '01' :
    if postNum2 in kangbuk :
        print('강북구')
    elif postNum2 in dobong :
        print('도봉구')
    else :
        print('노원구')


# 주민등록번호 유효성 체크
mul1 = [2, 3, 4, 5, 6, 7]
mul2 = [8, 9, 2, 3, 4, 5]
num = input('주민등록번호 : ')
num = num.split('-')
num1, num2 = num[0], num[1]
sum = 0

for i in range(6) :
    sum += int(num1[i]) * mul1[i] + int(num2[i]) * mul2[i]

result = sum % 11
result = 11 - result

if result == int(num2[-1]) :
    print('유효한 주민등록번호입니다')
else :
    print('유효하지 않은 주민등록번호입니다')


# 비트코인 가격
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = int(btc['max_price']) - int(btc['min_price'])
시가 = int(btc['opening_price'])
최고가 = int(btc['max_price'])

if 최고가 < 시가 + 변동폭 :
    print('상승장')
else :
    print('하락장')
