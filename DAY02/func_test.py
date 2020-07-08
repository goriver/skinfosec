# 함수정의 
# def 함수명(argument_list) 
# 구현 
#   return return_data

# def print_n_times(value, n):
#     for i in range(n):
#         print(value)



# # 함수사용
# # 함수명(argument_list) 반드시 argument 개수 일치해서 호출
# print_n_times("function",3)
"""
가변매개변수
: 매개변수를 원하는 만큼 받을 수 있는 함수
ex) print 내장 함수
* 해당 기호로 표기함
가변 매개변수 뒤에는 일반 매개변수 올 수 x
가변 매개변수는 하나만 사용할 수 있음

@ 가변 매개변수 사용시 argument_list는 0~ 임의의 수까지 써도 상관없다.
"""

# 가변매개변수 예시
def print_n_times(n, *values): # *변수명, #기본값 : 변수명 = 값
    for i in range(n):
        print(values)


print_n_times(3,"origin","가변매개변수")

# 기본매개변수 예시
def print_n_times(*values,n=2):
    for i in range(n):
        print(values)


print_n_times(3)
print_n_times(3,"origin","가변매개변수")
print_n_times(3, n=5)

"""
함수사용
함수명(argument_list) 반드시 argument 개수 일치해서 호출
가변 매개변수 사용 시 argument_list는 0..n
기본값에 명시된 변수명 = 사용자 정의값
"""

# return -함수종료
# return data -호출한 쪽에 데이터 전달, 
# return data,data - tuple 하나의 객체로 전달