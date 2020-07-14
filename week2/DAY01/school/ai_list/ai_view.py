# view : 입력하는 화면제공, 결과값 출력

# 메뉴 출력
def menu_display():
    print("========AI 수강생 관리 프로그램==========")
    print("1. 수강생 등록")
    print("2. 수강생 목록")
    print("3. 수강생 수정")
    print("4. 수강생 삭제")
    print("5. 수강생 검색")
    print("0. 종료")

# message 출력
def message_display(message):
    print(message)

# ai_list 목록 출력
def ai_list_display(ai_list):
    for index, ai_entity in enumerate(ai_list):
        print("{0}번째 : {1}".format(index, str(ai_entity)))

# ai_entity 상세정보 출력
def ai_entity_display(ai_entity):
    print("{0} 상세정보 : {1}".format(ai_entity.email,str(ai_entity)))

# 구분선
def line_display():
    print("="*30)
"""
view에는 출력 뿐만 아니라 입력 또한 포함된다
"""

# ai_entity 정보입력
def input_ai_entity():
    name = input("name : ")
    age = input("age : ")
    major = input("major : ")
    return name, age, major # 형식 지정 x -> tuple로 돌려준다
    

# email 정보 입력
def input_email():
    email = input("email : ")
    return email

# menu select 정보 입력
def input_select_menu():
    menu = input("메뉴를 선택하세요")
    return menu
