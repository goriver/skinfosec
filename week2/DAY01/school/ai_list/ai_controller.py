from ai_view import message_display, ai_list_display,ai_entity_display
import service
# view 입력된 데이터 체크, service의 business method 호출, 호출된 결과값 저장, view select
class AIController:

    # def __init__(self):
    #   super().__init__()


    def register_controller(self, ai_entity):
        # email vaild check - regular express사용 email형식 체크
        if (ai_entity.email == "" ) or (len(ai_entity.email) == 0):
            message_display("이메일 형식이 잘못됐습니다")
        else:
            bm = service.AIService() # service파일의 AIService 클래스 삽입
            message = bm.register(ai_entity)
            # view select
            message_display(message)

    def get_all_entity_controller(self):
        bm = service.AIService()
        bm_list = bm.get_all_entity()
        ai_list_display(bm_list)

    def ai_entity_update_controller(self,ai_entity):
        if (ai_entity.email == "" ) or (len(ai_entity.email) == 0):
            message_display("이메일 형식이 잘못됐습니다")
        else:
            bm = service.AIService() # service파일의 AIService 클래스 삽입
            message = bm.entity_update(ai_entity)
            # view select
            message_display(message)

    def delete_controller(self,email):
        if email == "" or len(email == 0):
            message_display("이메일 형식이 잘못됐습니다.")
        else:
            bm = service.AIService()
            message = bm.entity_remove(email)
            message_display(message)
    
    def get_entity_controller(self,email):
        if email == "" or len(email == 0):
            message_display("이메일 형식이 잘못됐습니다.")
        else:
            bm = service.AIService()
            ai_entity = bm.get_ai_entity(email)
            if ai_entity.email != "" and len(ai_entity.email):
                ai_entity_display(ai_entity)
            else:
                message_display("해당되는 데이터가 존재하지 않습니다.")

    def file_read(self):
        bm = service.AIService()
        bm.read_list()

    def file_write(self):
        bm = service.AIService() # service파일의 AIService()
        bm.save_list()