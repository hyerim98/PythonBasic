weather = input("오늘 날씨는? ")

if weather == "rain" or weather == "snow":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("날씨가 좋습니다")


temp = int(input("오늘의 기온은? "))
if 0<= temp < 10:
    print("외투 챙기세요")