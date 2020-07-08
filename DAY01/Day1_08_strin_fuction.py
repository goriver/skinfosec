""""
str = " 문자열 함수 알아보기 Hello Python "

print("lower : 소문자로 변경 ", str.lower())
print("upper : 대문자로 변경 ", str.upper())
print("strip : 양쪽 공백문자 제거", str.strip())
print("lstrip : 왼쪽 공백문자 제거", str.lstrip())
print("rstrip : 오른쪽 공백문자 제거", str.rstrip())

# in 연산자

print("안녕"in "안녕하세요")

# split() : 문자열 자르기
# 다른 언어에서  spit은 해당되는 특정 index에 일정 문자열을 추출
# or 배열의 데이터 조작을 위해서 사용

a = "동해물과 백두산이 마르고 닳도록 하느님이".split()
print(a) # ['동해물과', '백두산이', '마르고', '닳도록', '하느님이']
# 공백 기준으로 나눠짐

b = "동해물과|백두산이|마르고|닳도록|하느님이".split('|')
print(b) # ['동해물과', '백두산이', '마르고', '닳도록', '하느님이']

#part2 기억할 점
identifier 을 잘 기억하자(변수)
데이터 타입은 python은 저장 x 그러나 다르 ㄴ언어에서 있는 타입들이 다 있다
다른 언어랑 똑같이 산술 을 한다
특이한 것은 '//'이를 하면 나머지가 짤리는 것
단항 연산자같은 경우 c와 자바는 지원하는데 python은 안한다
데이터 타입이 틀리면 같은 숫자 타입이라면 묵시적으로 passup해서 한다. ex int float -> float으로
테스트를 위해서 내장 몇개를 써봤는데 print input 숫자인 문자열 타입은 외장함수 가지고 변환해서 사용
lower upper split truck split의 경우 다른 언어는 substring인데 여기서는 토큰을 가지고 문자의 데이터 값을 분리
예를 들어서 네트워크 파일 입출력의 경우라면 이러한 토큰을 가지고 분리시켜서 뽑아낼 수 있다.


# boolean

# 파이썬은 True False로 한다/ 
# 문자열은 기본적으로 유티코드 한바이트 2에 8승까지 아스키 코드가 기본 이로 숫자와 영문자 표현
# 인던트(indent) : 들여쓰기해서 하는 것 if문이던 뭐던

# datetime : 날짜 관련 모듈
# : 쓸 일이 많다
"""
"""
import datetime
now = datetime.datetime.now()

month = now.month
day = now.day
year = now.year
print(year,"년",month,"월",day,"일\n")


month = input("월을 입력해보세요")
if month == 1 \
    or month == 3\
    or month == 5\
    or month == 7\
    or month == 8\
    or month == 10\
    or month == 12:
    print("31일까지 있습니다")
else:
    print("30일까지 있습니다")
"""

def DayReturn(month):
    # month = input("월을 입력해보세요")
    if month == 1 \
        or month == 3\
        or month == 5\
        or month == 7\
        or month == 8\
        or month == 10\
        or month == 12:
        print("31일까지 있습니다")
    elif month ==2:
        print("28일까지 있습니다")
    else:
        print("30일까지 있습니다")

""" =============참고=============================================================
교재에서는 역슬래시 \로 함 근데 style guide에서는 아래와 같음. 괄호 안에 처리하는 방식

# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()
===============================================================================
"""
num = 0
while num <100:
    tmp_month = int(input("월을 입력해보세요!"))
    if tmp_month ==0:
        print("해당월은 달력에 없어요...ㅠ")
        continue
    elif tmp_month>12:
        print("해당월은 달력에 없어요...ㅠ")
        continue
    else:
        month = tmp_month
        DayReturn(month)
    num+=1




