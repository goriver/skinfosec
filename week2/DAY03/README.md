# SK infosec 클라우드 AI 전문가 양성과정

## WEEK 02
### 07/15
* readme.md 마크다운 첫 시작
* 마크다운은 jupyter의 마크다운 사용하면 편하당
* 어제) 도커 & 리눅스 명령어


## nginx 환경 구축
* nginx는 가장 많이 사용하는 웹 서버
* 1. nginx 설치
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

* 2. 이미지 실행하기
    * docker portforwarding을 해야한다. 왜냐하면 virture box를 사용하기 때문이다.
    * docker desktop 사용시에는 필요없다.
    * ![image](/uploads/9916194750dae2886a3836a5e223d81c/image.png)
    * vm ware에서 설정 > 네트워크 > 고급 > 포트 포워딩 > 다음과 같이 http , https 추가하기
    * ``` docker run --name webserver -d -p 80:80 nginx```
    * docker toolbox에 위와 같이 입력
    * 도커에서 내부적으로 쓰는 identifier을 생성해준다.
    * ![image](/uploads/da03feab75de8834487e047b84bb4ba0/image.png)
    - ps를 하면 우와 같이 설치 내역을 볼 수 있는데, docker ps -a로 치면 설치한 것들 다 나온다.
    - 교수님은 elegant_yalow 나는 peaceful_gagarin으로 출력된다 다 다르다

    * +a
    * __도커와 가상화와 차이점__
    - [설명 blog](https://medium.com/@darkrasid/docker%EC%99%80-vm-d95d60e56fdd)
    - 











                                                                