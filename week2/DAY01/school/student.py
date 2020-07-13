class Person:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    
    def __eq__(self,id):
        if(self.id == id):
            return True
        else:
            return False
            
    def info(self): 
        print("아이디:{0}\t이름:{1}".format(self.id,self.name),end = "")
    # def __str__(self): info대신 __str__로 쓸 수 있당 
    #         print("아이디:{0}\t이름:{1}".format(self.id,self.name),end = "")


class Student(Person):
    def __init__(self,id,name,major):
        super().__init__(id,name)
        self.major = major

    # def student_info(self):
    def info(self):
        super().info()
        print("전공 : {0}\t".format(self.major))

class Teacher(Person):
    def __init__(self,id,name,subject):
        super().__init__(id,name)
        self.subject = subject
    
    # def teacher_info(self):
    def info(self):
        super().info()
        print("담당과목 : {0}\t".format(self.subject))

class Employee(Person):
    def __init__(self,id,name,department):
        # self.id = id
        # self.name = name
        super().__init__(id,name)
        # 생성자 super은 자식 위에 놓아야 한다.
        self.department = department
    
    # def employee_info(self):
    def info(self):
        super().info()
        print("부서명 : {0}\t".format(self.department))

# ai01=Student("ai01","김주희","전자공학")
# ai01.student_info()

# ai_teacher = Teacher("T001","최재호","파이썬")
# ai_teacher.teacher_info()

# ai_employee =Employee("ai01","이준용","교육")
# ai_employee.employee_info()

"""
특이한 이름의 메소드
1> eq : equal
2> ne : not equal
3> gt : greater than
4> ge : greater than or equal
5> lt : less than
6> le : less than or equal


"""