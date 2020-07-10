# 수강생 관리 시스템 요구사항 추가하기
import os
import stu_fuction_module as st

global ai_list
st.start()
while(1):
    # 요기에 try ~// 1~5이외의 숫자는 except 적용하기

    print("====수강생 관리 시스템====")
    print("\t    1. 수강생 등록 \n \
           2. 수강생 목록 \n \
           3. 수강생 삭제 \n \
           4. 수강생 정보 수정 \n \
           5. 수강생 인덱스 확인 \n\
            0. exit")
    choice = int(input("선택하시오"))
    
    if choice == 1:
        name = input("이름입력 :")
        # 나이 숫자로 받아오기 -> try except 적용
        try:
            age = int(input("나이입력 :"))
            # break
        except:
            age = int(input("나이는 숫자로 입력해주세요"))
        major = input("전공입력 :")
        ai_dictionary={
            "name" : name,
            "age" : age,
            "major" : major
        }
        if st.register(ai_dictionary) =="success":
            print("정상적으로 저장되었습니다. \n")
        # continue
    elif choice == 2:
        print(st.all())
        # continue
    elif choice == 3:
        del_stu = input("삭제할 사람의 이름 입력")
        if st.ai_remove(del_stu) == "success":
            print("정상적으로 저장되었습니다. \n")
        # continue
    elif choice == 4:
        update_name = input("수정할 사람의 이름 입력")
        update_age =input("수정할 사람의 나이 입력")
        update_major = input("수정할 사람의 전공 입력")
        ai_dictionary = {
            "name" : update_name,
            "age" : update_age,
            "major" :update_major
        }
        # ai_update(ai_dictionary
        if st.ai_update(ai_dictionary)==1:
            print("정상적으로 저장되었습니다.\n")
        # continue

    elif choice ==5:
        find_name = input("확인할 사람의 이름 입력")
        st.ai_search(find_name)
        # continue
    elif choice ==0:
        print("=================종료=================")
        st.save_list(ai_list)
        break
    else:
        print("숫자는 1~5까지만 적어주세요")
        continue


"""
1. module화
- mvc에 맞게
- 기술에 따라서
2. try except
-1)
-2)
-3)
"""