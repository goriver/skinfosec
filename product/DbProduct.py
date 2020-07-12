import os

#ai_list ai_list.dat 파일저장
def save_list(prod_list):
    save_file = open("product_list.dat", "w")
    for index, value in enumerate(prod_list):
        save_file.write("{0}번째 | {1},{2},{3}\n".format(index, value["prod_num"],value["date"],value["brand"]))
    save_file.close()

#ai_list.dat 파일 내용 ai_list에 append
def read_data():
    prod_list =[]
    fileExist = os.path.isfile("product_list.dat")
    if fileExist:
        read_file = open("product_list.dat","r") 
        while True:
            prod_data = read_file.readline()
            if len(prod_data.split("|")) == 2 :
                prod = prod_data.split("|")[1].rstrip("\n").split(",")
                prod_list.append({"prod_num":prod[0].strip(),"date":int(prod[1].strip()),"brand":prod[2].strip()})
            if not prod_data: break
        print(prod_list)
        return prod_list
        read_file.close()

# def init(prod_list):
#     read_data(prod_list)
