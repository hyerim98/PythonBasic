import math


def std_weight(height, gender) :
    weight = height * height
    height = height * 100
    
    if gender == "남자" :
        weight = weight * 22
    elif gender == "여자" :
        weight = weight * 21
    else :
        print("성별이 잘못입력되었습니다.")
    
    print("키 %.1fcm %s의 표준 체중은 %.2fkg 입니다" %(height, gender, weight))

height = 163
std_weight(height / 100, "여자")