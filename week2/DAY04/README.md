# SK infosec 클라우드 AI 전문가 양성과정

## WEEK 02
### 07/16


* *복습) 도커 & 리눅스 명령어*

## DOCKERfile을 사용한 코드에 의한 서버 구축
### dockerfile을 사용한 구성 관리
1. dockerfile이란?
    *  docker상에서 작동시킬 컨테이너의 구성 정보를 기술하기 위한 파일
        - 강사님이 주신 js파일과 dockerfile 활용


* 1). 이미지 만들기
    - docker build (option) (생성할 이미지명): (버전정보) (dockerfile위치])
    - ```docker build -t nodeweb:1 .```
    - ![image](/uploads/bc76db34b236cdd3d04ee2aedb440ee2/image.png)
    - 위 이미지를 통해 확인할 수 있다.
    - 이미지 생성은 되었지만, container 생성한 것은 아니다.
* 2) 이미지 실행
    - ```docker container run --name nodeserver -d -p 80:80 nodeweb:1```
    - 이미지 실행(run)을 80포트에서 실행한다
    - <img src = "/uploads/dbca509f10b21935b36930f3df0a9fa2/image.png"> width = "60%" height="40%"></img>