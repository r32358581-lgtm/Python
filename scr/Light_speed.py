##
# 이 프로그램은 프록시마 센토리까지 빛이 가는 시간을 계산한다.
#
speed = 30000.0               # 빛의 속도
distance = 40000000000000.0   # 거리
secs =  distance / speed
light_year = secs / (60.0*60.0*24.0*365.0)
print(light_year, "광년")