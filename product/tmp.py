
# #제품번호등록 : 동일 제품명이 있는지 체크하고 message 리턴
# def register(prod_dic,prod_list):
#     index = is_exist(prod_dic["prod_num"],prod_list)
#     if index < 0 :
#        prod_list.append(prod_dic)
#        return prod_dic["prod_num"]+" 등록되었습니다."
#     else:
#         return prod_dic["prod_num"]+"님은 이미 등록되었습니다."

# #제품번호목록 : 리스트의 제품번호 목록 리턴
# def products(prod_list):
#     return prod_list

# #제품번호수정 : 제품번호검색 날짜, 브랜드 수정하고 message 리턴
# def prod_update(prod_dic,prod_list):
#     index = is_exist(prod_dic["prod_num"],prod_list)
#     if index > -1 : 
#         prod =prod_list[index]
#         prod["date"] = prod_dic["date"]
#         prod["brand"] = prod_dic["brand"]
#         return prod_dic["prod_num"]+"이 수정되었습니다."
#     else:
#         return prod_dic["prod_num"]+"정보는 존재하지 않습니다."

# #제품번호삭제 : 제품번호검색 리스트에서 삭제하고 message 리턴
# def prod_remove(prod_num,prod_list):
#     index = is_exist(prod_num)
#     if index > -1 :
#         prod_list.pop(index)  #ai_list.remove(ai_list[index])
#         return prod_num+"이 삭제되었습니다."
#     else:
#         return prod_num+"정보는 존재하지 않습니다."


# #제품번호검색 : 제품번호로 검색해서 dictionary 리턴
# def prod_search(prod_num,prod_list):
#     for index, value in enumerate(prod_list):
#         if value["prod_num"] == prod_num:
#             return value
#         else:
#             return prod_num+"정보는 존재하지 않습니다."

# #제품번호존재여부검색 : 제품번호로 검색해서 리스트의 index 값 리턴
# def is_exist(prod_num,prod_list):
#     for index, value in enumerate(prod_list):
#         if value["prod_num"] == prod_num:
#             return index
#     return -1

# ViewProduct로 이동
# def menu_display():
#     print("====  제품번호 관리 프로그램 =====")
#     print("1. 제품번호 등록")
#     print("2. 제품번호 목록")
#     print("3. 제품번호 수정")
#     print("4. 제품번호 삭제")
#     print("5.  검색")
#     print("0. 종료")

# def message_display(message):
#     print(message)

# #ai_list ai_list.dat 파일저장
# def save_list(prod_list):
#     save_file = open("product_list.dat", "w")
#     for index, value in enumerate(prod_list):
#         save_file.write("{0}번째 | {1},{2},{3}\n".format(index, value["prod_num"],value["date"],value["brand"]))
#     save_file.close()

# #ai_list.dat 파일 내용 ai_list에 append
# def read_data(prod_list):
#     fileExist = os.path.isfile("product_list.dat")
#     if fileExist:
#         read_file = open("product_list.dat","r")
#         while True:
#             prod_data = read_file.readline()
#             if len(prod_data.split("|")) == 2 :
#                 prod = prod_data.split("|")[1].rstrip("\n").split(",")
#                 prod_list.append({"prod_num":prod[0].strip(),"date":int(prod[1].strip()),"brand":prod[2].strip()})
#             if not prod_data: break
#         read_file.close()

# def init(prod_list):
#     read_data(prod_list)
prod_list = [{"prod_num":"prod_num", "date":"date", "brand":"brand"}]
prod_num = "prod_num"
for index, value in enumerate(prod_list):
    if value["prod_num"] == prod_num:
        print(type(value["prod_num"]))