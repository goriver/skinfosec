# try except
# print("==============================================")
# try:
#     print("입력받은 정수형 데이터 : {0}".format(int(data)))
# except:
#     print("{0}데이터 입력/ 정수를 입력하시오".format(data))
# finally:
#     print("항상 실행 구문")


# multi exception 처리
"""
try:

except ExceptionType as error1:
except ExceptionType as error2:
    ...

주의 : 자식 type의 ExceptionType부터 처리
"""
list_data = [10,20,30]
try:
    int_data = int(input("정수형 데이터 입력 : ")) # ValueError
    list_data.append(int_data)
    for index in range(len(list_data)):
        print("{0}번째 데이터 : {1}".format(index, list_data[index])) #IndexError
        # divide_sum = list_data[index]+list_data[index]/0 # ZeroDivisionError
        
except ValueError:
    print("정수를 입력해주세요")
    # print(type(exception),exception)
except IndexError:
    print("IndexError :  데이터 접근은 0~{0}까지 입니다.".format(len(list_data)-1))
except Exception as error:
    print(error, "프로그램에 문제가 있어 종료합니다.")