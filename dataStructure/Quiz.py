'''
    댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받는다

    조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
    조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가
    조건3 : random 모듈의 shuffle과 sample을 활용

    (출력 예제)
    -- 당첨자 발표 --
    치킨 당첨자 : 1
    커피 당첨자 : [2,3,4]
    -- 축하합니다 --
'''

from random import *

ids = range(1, 21) # 1 ~ 20까지의 숫자를 생성
ids = list(ids)
shuffle(ids)

winning = sample(ids, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : ", winning[0])
print("커피 당첨자 : ", winning[1:])
print("-- 축하합니다 --")