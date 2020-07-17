# import student

ai_list = [student.Student("ai01","김주희","전자공학"),student.Teacher("T001","최재호","파이썬"),student.Employee("ai01","김주희","전자공학")]
# ai01=student.Student("ai01","김주희","전자공학")
# ai01.student_info()

# ai_teacher = student.Teacher("T001","최재호","파이썬")
# ai_teacher.teacher_info()

# ai_employee =student.Employee("ai01","김주희","전자공학")
# ai_employee.employee_info()
"""
@ isinstance()함수

객체가 어떤 클래스로부터 함수를 가지고 있는지 체크
true / false로 답이 나옴
"""

for ai in ai_list:
    ai.info()



    # if(isinstance(ai,student.Student)):
    #     ai.student_info()
    # elif(isinstance(ai,student.Teacher)):
    #     ai.teacher_info()
    # elif(isinstance(ai,student.Employee)):
    #     ai.employee_info()
    # else:
    #     print("타입이 잘못되었습니다.")


