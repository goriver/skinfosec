# dictionary
ais_1={"name":"김주희","age":24,"major":"전자공학"}
ais_2={"name":"최재호","age":30,"major":"컴퓨터공학"}
ais_3={"name":"이준용","age":27,"major":"전기전자"}

ais = [ais_1, ais_2, ais_3] # 딕셔너리에 리스트를 넣어도되고, 반대로 리스트에 딕셔너리 넣어도 된다.
# print("ais_1 : 이름 {0}, 나이 {1}, 전공 {2}".format(ais_1["name"],ais_1["age"],ais_1["major"]))
ais_3["major"]="음악" # 값 변경
print("ais 신입사원 정보")
# sum = 1
for ai in ais:
    print(" 신입사원")
    print("이름 : {0}, 나이 : {1}, 전공 : {2}".format(ai["name"],ai["age"],ai["major"]))


print("ai 정보")
for key in ais_1:
    print("key : {0}, value : {1}".format(key, ais_1[key]))




# del : 요소제거
"""
del ais_1["age"] # 키로 값 이랑 키 제거
del ais_2["age"] # for문 돌려서 지워두 됨
del ais_3["age"]

for ai in ais:
    print(" 신입사원")
    print("이름 : {0},전공 : {1}".format(ai["name"],ai["major"]))
"""

#range
for i in range(len(ais)):
    print("{0}번째 : {1}".format(i, ais[i]))