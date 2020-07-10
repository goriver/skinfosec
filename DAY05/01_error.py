
# --------책 예제
list_input_a = ["52","273","32","스파이","103"]

list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        print("숫자가 아니에요")
        pass

print(list_input_a,"내부의 숫자는")
print(list_number,"입니다")

# 오류 발생 구문
print("==============================================")
data = input("정수입력 :")
"""

print("입력받은 정수형 데이터 : {0}".format(int(data)))

문자열 입력시 에러 : ValueError
"""
# 조건문으로 예외처리
print("==============================================")
if data.isdigit():
    print("입력받은 정수형 데이터 : {0}".format(int(data)))
else:
    print("정수를 입력하시오")

# try except
print("==============================================")
try:
    print("입력받은 정수형 데이터 : {0}".format(int(data)))
except:
    print("{0}데이터 입력/ 정수를 입력하시오".format(data))
finally:
    print("항상 실행 구문")
