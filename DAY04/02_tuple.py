"""
@@ 튜플

tuple_data= (10,20,30) # 리스트와 비슷한데 괄호와 쉼표를 활용해서 한다
tuple_data2= 10,20,30

print(tuple_data)
print(tuple_data2)

# 값 변경 testing
# tuple_data[0] =100 # TypeError: 'tuple' object does not support item assignment

# swapping
a,b = 10,20
print(a,b)
temp = a # 두개의 값 교환을 위한 임시 공간
a = b
b = temp
print(a,b)
# 튜플을 사용하면 쉽게 교환을 할 수 있다
a,b = 10,20
a,b = b,a # 튜플을 사용하면 swapping이 쉬워진다.
print(a,b)

@@ 
"""
