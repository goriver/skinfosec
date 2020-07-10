# 파일 처리

# @text data file 출력
write_file = open("hello.txt","w")
write_file.write("hello it's me python....")
write_file.close()

# @file 입력 -> consol
#>>> 리눅스 입력어>>>>
# 1. consol에 ls쳐서 dir 확인
# 2. cat 파일명 쳐서 파일내 내용 확인하기
read_file = open("hello.txt","r")
print("입력데이터 :",read_file.read())
read_file.close()

# @consol 입력 -> file 출력
read_data = input("파일에 입력할 데이터를 적어보세요")
write_file = open("hello.txt","w")
write_file.write(read_data)
write_file.close
print("파일을 성공적으로 저장하였습니다.")
# PS C:\skinfosec\python_workspace> cat hello.txt
# 안녕하세요 제 이름은 강가연입니다.

# @file입력->file출력
read_file =open("hello.txt","r")
write_file = open("copy_hello.txt","w") 
write_file.write(read_file.read())
read_file.close
write_file.close


# close를 같이 하고 싶다면 with키워드를 활용하라
# 