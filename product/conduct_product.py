import os.path
import ViewProduct
import DbProduct
import FunctionProduct as fp


"""
PM TODD / 기업 코드 작성 RULE
1 학생 관리 시스템에서 코드 수정. 
제품번호 -> name -> prod_num
브랜드 -> major -> brand
입고일 -> age -> date

2. MVC에 해당하는 클래스
    A) MODEL : -> view영역 select FunctionProduct as fp
    B) CONTROLLER : DbProduct -> db의 역할, file입출력 담당
    C) VIEW : ViewProduct -> front의 역할 보여지는 부분 담당

todo
1> 한개의 파일에서 돌아가는 제품 목록 리스트 체크하기
2> 3개의 파일로 쪼개기
3> pro_list : global선언하기 < 매개변수로 넘겨주기
"""


prod_list = DbProduct.read_data()
while True:
    
    ViewProduct.menu_display()

    menu = input("메뉴를 선택하세요 ")
    if menu == '1':
        prod_num = input("제품번호 : ")
        try:
            date = int(input("날짜 : "))
        except ValueError:
            print("숫자 형식에 맞추어 입력해주세요.")
        except:
            print("다시 입력해주세요. ex) 20200712")
        brand = input("브랜드 : ")
        prod_list = fp.register({"prod_num":prod_num,"date":date,"brand":brand},prod_list)
        # ViewProduct.message_display(message)
    elif menu == '2':
        ViewProduct.message_display("==== 제품번호 목록 ===")
        fp.products(prod_list) # 매개변수 prod_list
    elif menu == '3':
        prod_num = input("수정할 제품번호를 입력하세요 ")
        date = input("date : ")
        brand = input("brand : ")
        prod_list = fp.prod_update({"prod_num":prod_num, "date":date, "brand":brand},prod_list)
        # ViewProduct.message_display(message)
    elif menu == '4':
        prod_num = input("삭제할 제품번호를 입력하세요 ")
        prod_list = fp.prod_remove(prod_num,prod_list)
        # ViewProduct.message_display(message)
    elif menu == '5':
        prod_num = input("검색할 제품번호를 입력하세요 ")
        prod = fp.prod_search(prod_num,prod_list)  
        ViewProduct.message_display(prod)
               
    elif menu =='0':
        DbProduct.save_list(prod_list)
        break
    else:
        ViewProduct.message_display("메뉴는 1,2,3,4,5 중 하나를 선택하시고 종료를 원하시면 0번을 선택하세요")
    continue