#제품번호등록 : 동일 제품명이 있는지 체크하고 message 리턴
def register(prod_dic,prod_list):
    print(type(prod_dic["prod_num"]))
    index = is_exist(prod_dic["prod_num"],prod_list)
    if index < 0 :
       prod_list.append(prod_dic)
       print(prod_dic["prod_num"]," 등록되었습니다.")
       return prod_list
    else:
        print(prod_dic["prod_num"],"님은 이미 등록되었습니다.")
        return prod_list

#제품번호목록 : 리스트의 제품번호 목록 리턴
def products(prod_list):
    for prod in prod_list:
        print(prod)

#제품번호수정 : 제품번호검색 날짜, 브랜드 수정하고 message 리턴
def prod_update(prod_dic,prod_list):
    index = is_exist(prod_dic["prod_num"],prod_list)
    if index > -1 : 
        prod =prod_list[index] # prod 는 dictionary
        prod["date"] = prod_dic["date"]
        prod["brand"] = prod_dic["brand"]
        print(prod_dic["prod_num"],"이 수정되었습니다.")
        print(prod_list)
        return prod_list
    else:
        print(prod_dic["prod_num"],"정보는 존재하지 않습니다.")

#제품번호삭제 : 제품번호검색 리스트에서 삭제하고 message 리턴
def prod_remove(prod_num,prod_list):
    index = is_exist(prod_num,prod_list)
    if index > -1 :
        prod_list.pop(index)  #ai_list.remove(ai_list[index])
        print (prod_num," 삭제되었습니다.") 
        return prod_list
    else:
        print(prod_num,"정보는 존재하지 않습니다.")
        return prod_list

#제품번호검색 : 제품번호로 검색해서 dictionary 리턴
def prod_search(prod_num,prod_list):
    try:
        for index, value in enumerate(prod_list):
            if value["prod_num"] == prod_num:
                return value
            else:
                return prod_num+"정보는 존재하지 않습니다."
    except TypeError:
        print("'NoneType'입니다.")

#제품번호존재여부검색 : 제품번호로 검색해서 리스트의 index 값 리턴
def is_exist(prod_num,prod_list):
    for index, prod in enumerate(prod_list):
        if prod["prod_num"] == prod_num:
            return index
    return -1