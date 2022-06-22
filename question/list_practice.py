# list 추가
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)



# list 사이에 추가
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)



# 삭제
movie_rank.remove('럭키') # 1
# del movie_rank[3] # 2
print(movie_rank)

del movie_rank[2:] 
print(movie_rank)



# list 합치기
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang3 = lang1 + lang2
print(lang3)



# 최댓값, 최솟값 출력
nums = [1, 2, 3, 4, 5, 6, 7]
print('max: {0}'.format(max(nums)))
print('min: {0}'.format(min(nums)))



# list에 저장된 데이터의 개수 출력
list_len = len(nums)
print('count : ', list_len)



# list 합, 평균 출력
sum = sum(nums)
print('sum : ', sum)
print('avg : ', sum / list_len)



# list 슬라이싱
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2]) # 홀수 출력
print(nums[1::2]) # 짝수 출력
print(nums[::-1]) # 역방향 출력




# list안에 있는 데이터중에서 필요한 것만 출력
interest = ['삼성전자', 'LG전자', 'Naver']
del interest[1]
print(interest)



# Join
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))
print("/".join(interest))
print("\n".join(interest))


# Split
str = "삼성전자/LG전자/Naver"
interest = str.split('/')
print(interest)



# 리스트 정렬
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)




