# array = [273,32,103,57,52]
# for i in range(len(array)):
#     print(array[i])



# index = 0
# while index< len(ais) :
#     print("{0}번째 : {1}".format(index, ais[index]))
#     index +=1

# for i in range(1,11):
#     if i%2==0:
#         print(i,"는 짝수입니다.")
#     else:
#         print(i,"는 홀수입니다.")   
# print("====================================================")

# 구구단 출력
# # k=1
# for i in range(1,10):
#     for j in range(2,10):
#         print(j,"x",i,"=",i*j, end="\t")
#     print()
#     # 아항 j가 앞의 수로 가도 됨.

#dictionary
ais_1={"name":"김주희","age":24,"major":"전자공학"}
ais_2={"name":"최재호","age":30,"major":"컴퓨터공학"}
ais_3={"name":"이준용","age":27,"major":"전기전자"}

ais = [ais_1, ais_2, ais_3] # 딕셔너리에 리스트를 넣어도되고, 반대로 리스트에 딕셔너리 넣어도 된다.

# 이터레이트 객체를 반환해주는 enumerate를 많이 사용하게 될 것이다. 필수!
# enumerate
print("enumerate 함수 적용")
print(enumerate(ais)) # <enumerate object at 0x02F176E8>
print(list(enumerate(ais))) 
# 출력 [(0, {'name': '김주희', 'age': 24, 'major': '전자공학'}), (1, {'name': '최재호', 'age': 30, 'major': '컴퓨터공학'}), (2, {'name': '이준용
#', 'age': 27, 'major': '전기전자'})]

# items함수 활용하여 dic출력
print("===================================")
print("\nais_1 dictionary 정보 : items() 사용")
print(ais_1.items()) # dict_items([('name', '김주희'), ('age', 24), ('major', '전자공학')])
# 출력결과 튜플 형태로 들어가고 있음을 확인할 수 있다.
# 키와 값을 가져온다는 것 파악하기!!


"""
for i,value in enumerate(ais):
    print("{0}번째 사람정보 : {1}".format(i,value))
"""
#파이썬의 장점
# 1. list comprehension
# 리스트 내포
# for문을 이용해서 값을 조작하기 쉽다!