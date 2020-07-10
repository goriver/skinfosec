def add(value1,value2):
    return value1+value2

def subtract(value1,value2):
    return value1-value2

def multiply(value1,value2):
    return value1*value2

def divide(value1,value2):
    return value1/value2

print("calculator_module", __name__)
if __name__ == "__main__":
    print("calculator_module 엔트리포인트")
    

"""
엔트리포인트 모듈 역할을 할 모듈에 어플리케이션의 시작했을 때 구현해야할 부분을 모아둬라
"""
# if __name__ == "__main__":
#     pass
#  __name__ 변수의 값이 '__main__'인지 확인하는 코드는 
# 현재 스크립트 파일이 프로그램의 시작점이 맞는지 판단하는 작업입니다. 
# 즉, 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 
# 구분하기 위한 용도입니다.