ai_list =[]

def register(ai_dictionary):
    ai_list.append(ai_dictionary)
    return "success"

def all():
    for i, name in enumerate(ai_list):
        return print("{0}번째 학생 : {1}".format(i,ai_list[i])) 

def ai_remove(name):
    for ai in ai_list:
        if ai["name"]==name:
            del ai_list[ai_list.index(ai)]
            print("{0}이 정상적으로 삭제되었습니다.".format(name))
def ai_update(ai_dictionary):
    for i, ai in enumerate(ai_list):
            if ai["name"]==ai_dictionary["name"]:
                ai["age"]=ai_dictionary["age"]
                ai["major"]=ai_dictionary["major"]
                return "success"
            else:
                return "fail"

def ai_search(name):
    for i, ai in enumerate(ai_list):
        if ai["name"] == name:
            print("{0}번째 인덱스에 위치해있습니다.".format(i))
while(1):
    print("====수강생 관리 시스템====")
    print("\t    1. 수강생 등록 \n \
           2. 수강생 목록 \n \
           3. 수강생 삭제 \n \
           4. 수강생 정보 수정 \n \
           5. 수강생 인덱스 확인 \n\
           기타 : exit ")
    choice = int(input("선택하시오"))
    if choice == 1:
        name = input("이름입력")
        age = input("나이입력")
        major = input("전공입력")
        ai_dictionary={
            "name" : name,
            "age" : age,
            "major" : major
        }
        if register(ai_dictionary) =="success":
            print("정상적으로 저장되었습니다. \n")
    elif choice == 2:
        all()
    elif choice == 3:
        del_stu = input("삭제할 사람의 이름 입력")
        if ai_remove(del_stu) == "success":
            print("정상적으로 저장되었습니다. \n")
    elif choice == 4:
        update_name = input("수정할 사람의 이름 입력")
        if ai_update(update_name) == "success":
            print("정상적으로 저장되었습니다. \n")
    elif choice ==5:
        find_name = input("확인할 사람의 이름 입력")
        ai_search(find_name)
    elif choice ==6:
        print("=================종료=================")
        break
    else:
        print("숫자는 1~5까지만 적어주세요")
        continue
    