'''
    import만 사용하는 경우 
        패키지나 .py파일만 import 가능
'''
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

'''
    from 패키지나 .py파일 import Class명
'''
# from travel.vietnam import VietnamPackage
# trip = VietnamPackage()
# trip.detail()

'''
    travel 패키지 안에 있는 모든 것들을 import하겠다 라고 했지만, 오류가 발생한다
    패키지안에 import가 가능한 범위를 정의해줘야 한다(__init__)
'''
from travel import *
trip_to = thailand.ThailandPackage() # __init__ 파일에서 travel 패키지에서 외부에서 import 가능한 .py파일들 정의
trip_to.detail()