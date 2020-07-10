import math
import sys
import os

print(math.pi)
print(math.floor(50.555555))


"""
- 언어에 따라 외부 모듈 가져오는게 다르다.

* as 구문
@ math
import math as m
m.sin(1)
단점> 유지보수 및 운영자의 입장에서는 코드 볼때 가독성이 떨어질 수 있다.
해결책> 코딩가이드로 정해서 해야함

@ random
seed를 사용하지 않은 random함수를 사용하면 어느정도 예측 가능한 난수가 나온다.
따라서 무식하게 random만 가지고 하지는 않고 보통은 seed를 주고 구한다.

@ sys module

"""
print(sys.argv)