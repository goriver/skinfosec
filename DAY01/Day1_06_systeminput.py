# #01
# hello = input("인삿말입력 : ")
# print(type(hello))
# #input 타입으로 받아오는 경우, 모든 값은 str로 변환되어 받아온다

# #02
# input - sys.in 표준 콘솔로부터 문자열로 데이터 입력
# num = input("add number : ")
# print(int(num)+100) # 숫자문자 아닌 문자인 경우 ValueError

# 03 두개의 문자를 받아서 덧샘 출력하기
num1 = int(input("첫번째 문자 : "))
num2 = int(input("두번째 문자 : "))


# print(int(num1)+int(num2))
print(num1+num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
print(num1%num2)