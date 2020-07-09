# 람다

# • 기능을매개변수로전달하는코드를더효율적으로작성

def increase(value,original):
    return original+value

original_list = [10,20,30,40,50]
print("before",original_list)

for index, value in enumerate(original_list):
    original_list[index] = increase(5, value)
print("after ",original_list)

"""
# map : function을 매개변수로 받음
# filter : 두 함수는 function 매개변수에 집어넣어서 쉽게 사용 가능하다
"""
print("================매개변수에 함수 호출===============")

# def increase(value):
    # return value+10

def decrease(value):
    return value-10

original_list = [10,20,30,40,50]
print("original list",original_list)

# new_list =map(increase(), original_list) # <map object at 0x0314B058>
# print("map 실습 ",list(new_list))

def call_changedata(func,original_list): # 데이터 변수처럼 func 활용
    new_list=[]
    for index, value in enumerate(original_list):
        new_list.append(func(value))
    
    return new_list

print("new_list : ",call_changedata(increase,original_list))
print("new_list : ",call_changedata(decrease,original_list))
# call_changedata(increase,10)
# call_changedata(decrease,5)

print("================= map활용 ====================")
print("new_list", list(map(increase,original_list)))
print("new_list", list(map(decrease,original_list)))

print("================= lambda활용 ====================")
print("new_list", list(map(lambda value: value+10,original_list)))
print("new_list", list(map(lambda value: value-10,original_list)))

print("================= filter활용 ====================")
print("new_list", list(filter(lambda value: value<30,original_list))) # 30 미만의 값만 돌려준다
print("new_list", list(filter(lambda value: value>30,original_list))) # 30 초과의 값만 돌려준다


"""
# map 함수
내장함수
입력받은 자료형의 각 요소가 합수에 의해 수행된 결과를 묶어서 map iterator 객체로 리턴

# 문법
map(f, iterable)
# 함수(f)와 반복 가능한 (iterable) 자료형을 입력으로 받는다.

# lambda 인수1, 인수2, ... : 인수를 이용한 표현식
~> sum = lambda a, b: a+b
~> sum(3,4)
7

# filter 함수
filter(함수, literable)
두번째 인수인 반복 가능한 자료형 요소들을 첫번째 인자 함수에 하나씩 입력하여 리턴값이 참인 것만 묶어서 돌려준다.
함수의 리턴 값은 참이나 거짓이어야 한다.
"""
