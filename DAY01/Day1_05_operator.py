# 단항연산자 부호
value = 0
print(-value)

# 이항연산자 : 산술연산자 : -,+,*,/,//,%
#             논리연산자 : and or not
#             관계연산자 : >,<,>=,<=,!=
#             대입연산자 : =, +=, -=, 

#=========================================================================================

#PI=3.142592일때 원의 넓이와 둘레 구하는 연산

r = 5
pi=3.142592

# 원의 넓이
roundVolume = r*2*pi 
# 원의 둘레
roundLenght = r**2*pi

print("원의 넓이 : {0}\n원의 둘레 : {1}".format(roundVolume,roundLenght))