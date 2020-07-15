# SK infosec 클라우드 AI 전문가 양성과정

## WEEK 02
### 07/15
* readme.md 마크다운 첫 시작
* 마크다운은 jupyter의 마크다운 사용하면 편하당
* 어제) 도커 & 리눅스 명령어

## DOCKER 명령
### nginx 환경 구축
* nginx는 가장 많이 사용하는 웹 서버
1. nginx 설치
    *  도커허브에 검색 후 설치
        * 방법 1
        * ``` $ docker run --name some-nginx -v /some/content:/usr/share/nginx/html:ro -d nginx ```
            * docker (container) run ~~~
        * 방법 2
        * ``` FROM nginx```
        * ```COPY nginx.conf /etc/nginx/nginx.conf```
    * 도커 toolbox에 설치 
    * ``` $ docker nginx```
    * 도커 desktop에서는 검색 중 nginx에 넣어둔다

* * * 

### Docker 이미지 조작
1. 이미지 실행하기
    * docker portforwarding을 해야한다. 왜냐하면 virture box를 사용하기 때문이다.
    * docker desktop 사용시에는 필요없다.
    * <img src ="/uploads/9916194750dae2886a3836a5e223d81c/image.png" width="450px"height="300px"title="docker설정"alt="docker01">
    * vm ware에서 설정 > 네트워크 > 고급 > 포트 포워딩 > 다음과 같이 http , https 추가하기
    * ``` docker run --name webserver -d -p 80:80 nginx```
    * docker toolbox에 위와 같이 입력
    * 도커에서 내부적으로 쓰는 identifier을 생성해준다.
    *  <img src ="/uploads/da03feab75de8834487e047b84bb4ba0/image.png" width="450px"height="300px"title="docker설정"alt="docker01">
    - ps를 하면 위와 같이 설치 내역을 볼 수 있는데, docker ps -a로 치면 설치한 것들 다 나온다.
    - 컨테이너 명 미설정시 : 교수님은 elegant_yalow 나는 peaceful_gagarin으로 출력된다 다 다르다
    - ![image](/uploads/20500f5ea52fc36a40ceb1d328f66202/image.png)
    - 로컬호스트 접속시 해당 페이지 오픈
    - 80:80으로 run중이라서 이렇게 뜨고 있다.

2. 도커 컨테이너 확인
    * <img src = "/uploads/5dce636c15c68fd43bf68902d8907ed9/image.png" width="450px" height="350px"></img>
    * 실행중인 container확인  
        - docker ps
        - docker ps -a
    * exited된 컨테이너 삭제
        - docker rm container-name
        - docker rm helloworld
        - docker ps -a
    * container 명 변경 
        - docker rename container -name container-rename
    * container 중지
        - docker stop container web
        - docker stop web
    * container 실행
        - docker start web
    
    * __+alpha__
    * __도커와 가상화와 차이점__
    - [설명 blog](https://medium.com/@darkrasid/docker%EC%99%80-vm-d95d60e56fdd)
    - 시험 삘
* * * 

## DOCKERFILE을 사용한 코드에 의한 서버 구축

1. 도커 contos설치
    * ubuntu, centos:7 image download
    - ```docker pull ubuntu```
    - ```docker pull centos:7 #centos:version(tag)   ```

    * image 상세보기 - __image config Dockerfile 조회__
    - ```docker image inspect ubuntu```
    - <img src = "/uploads/f75ea69d2478259083874776872deca1/image.png" height = "180" width="120"></img>

    * image 삭제 - __image 사용하는 container가 있는 경우 사용하는 container삭제후 사용 가능하다. 
    - ```docker image rm imageID ```

    * 사용하지 않는 image삭제
    - ```docker image prune```
    
    * ubuntu, centos:7 container 생성/실행(create/start)
    * centos의 /bin/cal --calendar 실행 -it:표준입출력 사용
    - ``` docker run -it --name centos_cal centos:7 /bin/cal ```
    - ``` docker ps -a```
    - ``` docker run -it --name centos_shell centos:7 bin/bash ```
    - ``` root@:/#adduser test1 //test1 user 생성```
    - ``` root@:/#su test       //test1 user로 변경```
    - ``` testQ:/$ ls -al       //목록보기 ```
    - ``` testQ:/$ exit         // root로 가기 ```
    - ``` test@:/# exit         // docker로 가기 ```

    - ``` docker pa -a          // centos_shell은 exited상태```
    - ``` root@:/#              // ctrl+p+q docker로 가기```
    - ``` docker attach centos_shell``` // root로 
    - ``` root@:/#```

    - ctrl+p+q 누르면 ```root@ef00077585d2:/# read escape sequence```이렇게 출력되고 나오게 만든다
    * 도커를 이용하면 attach를 이용해 이거저거 쓰기 좋다.

    * apt-get -> pip과 같은 기능을 한다. 설치할 때 쓰인다.
    - ![image](
    - <img src = "/uploads/da213a7b63a1efe2c8be0b63a263d889/image.png" width="120",height="80"></img>
    - __앞으로는 운영 및 시스템도 코딩해야한다.__ 위와 같이 `기호를 활용하여 두개의 동작을 한꺼번에 같이 진행할 수 있다.
    - ![image](/uploads/59880acda5b41241a7e5c6a089886415/image.png)
    - 이렇게 쳐야한다. 역시 또 오타나서 다경언니가 해결해주셨당...ㅎㅎㅎㅎ
* * *
### centos
* centos는 ubuntu와 다른 문법 사용한다. but 뿌리는 리눅스이다.



    - 여기서는 나갈려면 :wq : 저장하고 나가기 하기
    * __vi editor__
    - [vi editor 링크](https://wiki.kldp.org/KoreanDoc/html/Vim_Guide-KLDP/Vim_Guide-KLDP.html)

* <img src ="/uploads/33bbd1dcda33928c2b43812fc61c6ff9/image.png"width="150"height="130">










                                                                