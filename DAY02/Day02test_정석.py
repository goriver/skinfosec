ai_list = []

while(1):
    print("====수강생 관리 시스템====")
    print("\t    1. 수강생 등록 \n \
           2. 수강생 목록 \n \
           3. 수강생 삭제 \n \
           4. 수강생 정보 수정 \n \
           5. 종료")
    choice = int(input("선택하시오"))
    if choice == 1:
        name = input("이름입력")
        age = input("나이입력")
        major = input("전공입력")
        stu_info = {
            "name":name,
            "age":age,
            "major":major
        }
        ai_list.append(stu_info)
    elif choice == 2:
        print(list(enumerate(ai_list)))
    elif choice == 3:
        del_stu = input("삭제할 사람의 이름 입력")
        for ai in ai_list:
            if ai["name"]==del_stu:
                del ai_list[ai_list.index(ai)]
    elif choice == 4:
        corr_stu=input("수정할 사람의 이름 입력")
        # c_name=input("이름 입력")
        c_age=input("나이 입력")
        c_major=input("전공 입력")
        for ai in ai_list:
            if ai["name"]==corr_stu:
                ai["age"]=c_age
                ai["major"]=c_major
    else:
        break