# 슬라이싱 + 반복문
list = ["가", "나", "다", "라"]
for str in list[::2] :
    print(str)

print()

for str in list[::-1] :
    print(str)




# 특정 조건에 해당하면 출력
nums = [3, -20, -3, 44]
for n in nums :
    if n < 0 :
        print(n)


nums = [13, 21, 12, 14, 30, 18]
for n in nums :
    if (n < 20) and (n % 3 == 0) :
        print(n)


# 첫 문자를 대문자로 변경 
animal = ['dog', 'cat', 'parrot']
for a in animal :
    print(a.capitalize())


# split() : 확장자 제거하고 파일 이름만 출력
files = ['hello.py', 'ex01.py', 'intro.hwp']
for file in files :
    file = file.split('.')[0]
    print(file)


# endwith() : 확장자가 .h인 파일 이름을 출력
files = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file in files :
    if file.endswith('.h') :
        print(file)


# range(시작, 끝, 증감)
for year in range(2002, 2051, 4) :
    print(year)


# range() : 감소
for i in range(99, 0, -1) :
    print(i)




# 2차원 리스트
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

result = []

for line in data :
    res = []
    for col in line :
        res.append(col * 1.00014)
    result.append(res)
print(result)


# 2차원 리스트 + 슬라이싱
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:] :
    print(i[3])

profit = 0
for i in ohlc[1:] :
    profit += i[3] - i[0]
print(profit)
