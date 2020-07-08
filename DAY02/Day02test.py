# 실습 예제 테스트

# def inroll(name,age,major):
    # print("수강생 정보를 입력하시오")
    # name = input("이름 : ")
    # age = input("나이 : ")
    # major = input("전공 : ")
    # dict_st = {
    #     "이름": name,
    #     "나이": age,
    #     "전공":major
    # }
ai_list =[]
while True:
    print("------메뉴를 선택하세요-------")
    print("1.AI 수강생 등록 \n2. AI수강생 목록")
    print("3. 수강생 삭제")
    print("4. 수강생 정보 수정")
    print("5. 종료")

    choice=int(input("메뉴 number을 고르세요"))
    if choice ==1:
        print("수강생 정보를 입력하시오")
        name = input("이름 : ")
        age = input("나이 : ")
        major = input("전공 : ")
        # inroll(name,age,major)
        dict_st = {
            name : [age,major] # 해결책 : 이름을 key로 만든다.
            }
        ai_list.append(dict_st)        
    elif choice ==2:
        print(list(enumerate(ai_list)))
    elif choice ==3:
        del_name = input("삭제할 이름을 입력하세요")
        for ai in ai_list:
            if del_name in ai.keys():
                del ai[del_name]         
    elif choice ==4:
        corr_name = input("수정할 이름을 입력하세요")
        for ai in ai_list:
            if corr_name in ai.keys(): # 전제 : 
                age = input("수정할 나이")
                major = input("수정할 전공")
                ai[corr_name] = [age,major] 
            """ 루다's dict안에 name, age, major 다 있음
            if(ai["name" == corr_namecorr_name):
                del ai_list[ai_list.index(i)]
                index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.
            """
    elif choice ==5:
        break