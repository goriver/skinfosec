class AIEntity: 
# 축약어는 보통 대문자

    # 생성자정의 : member, variable - name, age, email, major
    def __init__(self,name,age,email,major):
        self.name = name
        self.email = email
        self.age = age
        self.major = major
    # override : email정보가 같은 경우 같은 객체로 재정의
    def __eq__(self,email):
        if self.email == email:
            return True
        else:
            return False

    def __str__(self):
        return "{0} : {1} : {2} : {3}".format(self.name, self.email, self.age, self.major)


    #toJson   : Entity -> json 변환
    #fromJson : json -> Entity 변환