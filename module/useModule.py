'''
    모듈 사용법 1
'''
# import theater_module

# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_solider(5)

'''
    모듈 사용법 2
'''
# import theater_module as mv

# mv.price(3)
# mv.price_morning(4)
# mv.price_solider(5)


'''
    모듈 사용법 3
'''
# from theater_module import *
# price(3)
# price_morning(4)
# price_solider(5)

'''
    모듈 사용법 4
'''
# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# # price_solider(5) # 오류 발생

'''
    모듈 사용법 5
'''
from theater_module import price_solider as ps
ps(5) # 군인 할인 가격 출력
