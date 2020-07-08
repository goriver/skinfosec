"""
동일한 데이터 타입의 저장공간을 만들어서 
처리하면 쉽고 편하당. 배열에 담는 데이터도 type에 의존적이지 않다.
python은 해당되는 저장공간에 중복만되지 않는다면 서로 다른 데이터 타입을 저장할 수 있다.
array가 아니라 list로 생각(java)
"""

# array_list = [12,10,"홍길동",True,"홍길동"]
# array_list
# print(array_list)
# print(type(array_list))

"""
부모타입의 학생, 자녀 담아야하는데
이는 다형성에 의해서 부모타입으로 해서 
이는 자식타입의 형태가 부모타입으로 하면 비유를 들자면 해당 부모타입으로 상속을 하시면 부모타입으로 핸들링 가능하다
궁극적으로 이러한 언어를 훨씬 많이 쓸 것이다.
엄밀하게 따지면 해당되는 데이터를 가르킨다고 이해하면 된다.
class타입일 경우 마찬가지로 object의 데이터가 들어간 곳에 레퍼런스가 있을 것이다.

인덱스는 역시 0부터 시작하닌깐 0이 넘어가면 마찬가지로 인덱스 에러가 발생한다. -인덱스도 마찬가지로 뒤에서부터 돈다


"""
# array_list[0] = 20
# print(array_list)

# array_list[0] = 12.5
# print(array_list)

# array_list[0] = 2
# print(array_list)


list_array =[[1,2,3],[4,5,6,"data"]]
print(type(list_array))
print(type(list_array[0]), len(list_array[1]))
print(type(list_array[0][1]))
