# SK infosec 클라우드 AI 전문가 양성과정

## WEEK 02
### 07/16


* *복습) 도커 & 리눅스 명령어*

## DOCKERfile을 사용한 코드에 의한 서버 구축
### dockerfile을 사용한 구성 관리
1. dockerfile이란?
    *  docker상에서 작동시킬 컨테이너의 구성 정보를 기술하기 위한 파일
        - 강사님이 주신 js파일과 dockerfile 활용


    __1). 이미지 만들기__
    - docker build (option) (생성할 이미지명): (버전정보) (dockerfile위치])
    - ```docker build -t nodeweb:1 .```
    ![image](/uploads/bc76db34b236cdd3d04ee2aedb440ee2/image.png)
    - 위 이미지를 통해 확인할 수 있다.
    - 이미지 생성은 되었지만, container 생성한 것은 아니다.   



    __2) 이미지 실행__
    - ```docker container run --name nodeserver -d -p 80:80 nodeweb:1```
    - 이미지 실행(run)을 80포트에서 실행한다
<<<<<<< HEAD
    - <img src = "/uploads/dbca509f10b21935b36930f3df0a9fa2/image.png"> width = "60%" height="40%"></img>       
    __3) constiner 확인__
=======

    - <img src = "/uploads/dbca509f10b21935b36930f3df0a9fa2/image.png"> width = "60%" height="40%"></img>   



    __3) constiner 확인__
    
    - <img src = "/uploads/dbca509f10b21935b36930f3df0a9fa2/image.png" width = "60%" height="40%"></img>   
* 3) constiner 확인
>>>>>>> d82fdf65ce7ecb8fb21ebc14dd84b25261fe7c11
    - ```docker exec -it nodeserver bash ```
    - 위와 같은 코드를 입력하면 root@로 떨어진다.
    ![image](/uploads/230861b5ce7e6d284f7af0ded0d45cd8/image.png)
    - cat으로 etc/issue를 확인하면 debian 운영체제임을 확인할 수 있다.
    ![image](/uploads/9480c985143ba5fbe8e982cc498ec7db/image.png)
    - 이렇게 app js가 있는 것을 확인하고 cat을 활용해 사용되고 있는 코드를 확인 할 수 있다.   



    __4) app.js copy하기__
    ![image](/uploads/91000bd96424a1760239a4c86f5a542b/image.png)
    - image 내용 copy한 파일 확인 가능!
    ![image](/uploads/3805bacabba10d08852d1618c471d5e3/image.png)
    - 반대로 txt파일을 docker에 copy할 수도 있다.  



    __5) go언어로 해보기__
    - node.js와 달리 go, python, java는 vertual muchine이나 webserver가 필요하다. (ex. 장고 프레임워크 등등)
    - go 언어 : 구글 개발한 언어, 최근 가장 핫함
    - python보다 빠르고, java보다 쉽다
    - *Go (golang) is a general purpose, higher-level, imperative programming language.*
    - *Go (a.k.a., Golang) is a programming language first developed at Google. It is a statically-typed language with syntax loosely derived from C, but with additional features such as garbage collection, type safety, some dynamic-typing capabilities, additional built-in types (e.g., variable-length arrays and key-value maps), and a large standard library.*
<<<<<<< HEAD
    <img src = "/uploads/c16fd6253f894aeb8217eb4ea7116541/image.png" height="320%" width = "40%"></img>
=======

    - <img src = "/uploads/c16fd6253f894aeb8217eb4ea7116541/image.png" height="320%" width = "40%"></img>
    - <img src = "/uploads/c16fd6253f894aeb8217eb4ea7116541/image.png" height="30%" width = "40%"></img>
>>>>>>> d82fdf65ce7ecb8fb21ebc14dd84b25261fe7c11
    - 솔직히 go언어 오늘 youtube에서 보고 배우고 싶다고 생각해서ㅠㅠㅠㅠㅠ 완전 운이 좋았다고 생각한다.
***

### docker layer의 이미지 구조

* p159
    * ubuntu 위에 nginx html 설치하기 
    * 인덱스 파일 만들어서 build 실습하기    

    - Dockerfile은 D 대문자를 꼭 주자 왜냐하면 파일명을 처음에 설정 안해놔서 Default로 Dockerfile로 설정되어 있다.
*** 

* nginx
    - 운영체제를 가장 기본 기능만 넣는 것이다.



##### 실습
* 생성된 이미지 파일 실행 - welcome page html 띄워보기



    * image 생성
    - ``` docker build -t unginweb:1``` 여기서 unginweb은 내가 설정한 이미지 명이다.
    * image 확인
    - ``` docker images```
    * container 생성 및 실행
    - ``` docker run --name unginxserver -d -p 80:80 unginxweb:1 ```
    * local host에 바꾸기
    - ```curl localhost```
    * *오류 내용* 이전에 실행한 컨테이너로 이미지가 겹치는 문제가 발생했다
    - *해결책* 컨테이너 실행 중지 후 다시 실행. multi로 겹치면 강제로 삭제후 다시 실행
    
    - 위 해결책으로 하면 nginx의 default로 출력됨 이를 bash에서 수정해줘야함
    * bash 실행
    - ```docker exec -it unginxserver bash```
    - @root# ```ls al /usr/share/nginx/html```
    - @root# ```mv /usr/share/nginx/html/index.html /var/www/html/``` 새로 만든 index.html을 nginx서버와 연결해야한다.
    - @root# ```exit```
    * bash 수정 내용 다시 localhost에 반영
    - ```curl localhost```
***
***
***

## DB - MYSQL

### DOCKER에서 MYSQL 다운로드
* mysql docker로 다운받는 법
    1. docker hub 검색 후 다운로드
    ![image](/uploads/e3f08395485d534a3905e77dd5a52392/image.png)
    - image로 pull한 다음에 확인한다
    2. container 생성/실행
    - ```docker run --name mysql5 -e MYSQL_ROOT_PASSWORD=password -d -p  3306:3306 mysql:5.7```
    - up상태인 것을 확인 가능하다 (docker ps로 확인!)
    3. container 명령 실행
    ``` docker exec -it mysql5 bash```
    4. container 실행후 mysql 실행 가능한지 확인하기
    <img src = "/uploads/b5e9f12a9e326cbefe41124f2be53792/image.png" width = "45%" height = "30%"></img>
    [mysql튜토리얼](https://dev.mysql.com/doc/refman/5.7/en/tutorial.html)
    - root@f0afcba60146:/# ```mysql -u root -p```
    - Enter password : ```password```
    - 이렇게 password를 입력해준다
    - 이제 password까지 입력하면 mysql로 넘어가는데 이때 ```show databases;```를 입력하게 되면 SQL을 보여준다.
    ![image](/uploads/71048beccb6e8a2ed0a220a69b71c45a/image.png)
    - show databases를 입력하면 현존하는 데이터베이스 목록을 보여주게 된다.
    - 즉, __데이터베이스 목록을 조회하는 SQL문__ 으로 생각하면된다
    - sql은 알아야지 적어도 db를 다룰 수 있다.
    - information_schema :  데이터에 의한 데이터로써 즉 메타 데이터(Meta Data)로써 데이터 사전이다. 데이터 사전(Data Dictionary)이란 데이터베이스에 속한 데이터들의 정보를 저장한 것으로써, 시스템 카탈로그(System Catalog)라고도 한다. 
    - performance_schema : MySQL의 성능과 관련된 정보
    - [쿼리연습](https://www.w3schools.com/sql/default.asp)