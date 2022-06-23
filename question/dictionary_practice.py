# star expression 사용
from unittest import result


scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)

a, b, *valid_score = scores
print(a)
print(valid_score)

a, *valid_score, b = scores
print(valid_score)
print(b)




# dictionary 생성
iceCream = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(iceCream)

# dictionary 값 추가
iceCream['죠스바'] = 1200
iceCream['월드콘'] = 1500
print(iceCream)


# dictionary value 출력
print('메로나 가격 : ', iceCream['메로나'])

# dictionary value 수정
iceCream['메로나'] = 1300
print(iceCream)

# dictionary 값 삭제
del iceCream['메로나']
print(iceCream)



# dictionary + list 생성
inventory = {'메로나' : [300,20], '비비빅' : [400,3], '죠스바' : [250,100]}
print(inventory)

print('메로나 가격 : {}원'.format(inventory['메로나'][0]))
print('메로나 재고 : {}개'.format(inventory['메로나'][1]))

inventory['월드콘'] = [500,7]
print(inventory)


# keys, values 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice_key = list(icecream.keys())
print(ice_key)

ice_value = list(icecream.values())
print(ice_value)

print('아이스크림 총 금액 : {}원'.format(sum(ice_value)))


# update : dictionary + dictionary 합치기
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)


# dict, zip : 2개의 tuple을 하나의 dictionary로 변환
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)