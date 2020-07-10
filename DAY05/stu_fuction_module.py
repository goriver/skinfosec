# ai_list =[]
# 1. 수강생 등록
def register(ai_dictionary):
    # try:
    #     ai
    ai_list.append(ai_dictionary)
    return "success"

def start():
    # init()
    # for i, name in enumerate(ai_list):
    #     print("{0}번째 학생 : {1}\n".format(i,ai_list[i])) 
    stu_file = open("stu_list.txt","r")
    # stu_file = list(stu_file)
    with open('stu_list.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    # lines = stu_file.readlines()
    for line in lines:
        # for i,li in enumerate(line):
        #     print("{0}번째 학생 : {1}".format(i,li))
        ai_list.append(line)

def all():
    for i, ai in enumerate(ai_list):
        print("{0}번째 info : {1}".format(i,ai))

def ai_remove(name):
    for ai in ai_list:
        if ai["name"]==name:
            del ai_list[ai_list.index(ai)]
            print("{0}이 정상적으로 삭제되었습니다.".format(name))
        # return 1
def ai_update(ai_dictionary):
    for ai in ai_list:
        if ai["name"]==ai_dictionary["name"]:
            ai["age"]=ai_dictionary["age"]
            ai["major"]=ai_dictionary["major"]
            return 1
    # return 1

def ai_search(name):
    for i, ai in enumerate(ai_list):
        if ai["name"] == name:
            print("{0}번째 인덱스에 위치해있습니다.".format(i))

def save_list(ai_list):
    for ai in enumerate(ai_list):
        with open("stu_list.txt","w") as file:
            file.write("{0} \n".format(ai))

if __name__ == "__main__":
    pass