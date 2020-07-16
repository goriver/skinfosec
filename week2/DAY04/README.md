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
    - <img src = "/uploads/dbca509f10b21935b36930f3df0a9fa2/image.png" width = "60%" height="40%"></img>   
* 3) constiner 확인
    - ```docker exec -it nodeserver bash ```
    - 위와 같은 코드를 입력하면 root@로 떨어진다.
    - ![image](/uploads/230861b5ce7e6d284f7af0ded0d45cd8/image.png)
    - cat으로 etc/issue를 확인하면 debian 운영체제임을 확인할 수 있다.
    - ![image](/uploads/9480c985143ba5fbe8e982cc498ec7db/image.png)
    - 이렇게 app js가 있는 것을 확인하고 cat을 활용해 사용되고 있는 코드를 확인 할 수 있다.   
* 4) app.js copy하기
    - ![image](/uploads/91000bd96424a1760239a4c86f5a542b/image.png)
    - image 내용 copy한 파일 확인 가능!
    - ![image](/uploads/3805bacabba10d08852d1618c471d5e3/image.png)
    - 반대로 txt파일을 docker에 copy할 수도 있다.   
* 5) go언어로 해보기
    - node.js와 달리 go, python, java는 vertual muchine이나 webserver가 필요하다. (ex. 장고 프레임워크 등등)
    - go 언어 : 구글 개발한 언어, 최근 가장 핫함
    - python보다 빠르고, java보다 쉽다
    - *Go (golang) is a general purpose, higher-level, imperative programming language.*
    - *Go (a.k.a., Golang) is a programming language first developed at Google. It is a statically-typed language with syntax loosely derived from C, but with additional features such as garbage collection, type safety, some dynamic-typing capabilities, additional built-in types (e.g., variable-length arrays and key-value maps), and a large standard library.*
    - <img src = "/uploads/c16fd6253f894aeb8217eb4ea7116541/image.png" height="320%" width = "40%"></img>
    - 솔직히 go언어 오늘 youtube에서 보고 배우고 싶다고 생각해서ㅠㅠㅠㅠㅠ 완전 운이 좋았다고 생각한다.
    - 

