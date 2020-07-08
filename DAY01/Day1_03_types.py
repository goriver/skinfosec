name="이준용"
age=27
height=180.9
skinfosec=True
#for문으로 돌리기
servey = [name,age,height,skinfosec]
for i in servey:
    print(type(i))

# 한줄 출력
print(type(name),type(age),type(height),type(skinfosec))

# print("안녕하세요"[5]) IndexError: string index out of range

def calculator(xtype):
    if xtype =="+":
        