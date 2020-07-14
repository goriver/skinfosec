# SK infosec 클라우드 AI 전문가 양성과정

## WEEK 02
### 07/14
* readme.md 마크다운 첫 시작
* 마크다운은 jupyter의 마크다운 사용하면 편하당

## docker 설치 및 운영 계획
![image](/uploads/4acbd46102919f769b48312216fc0111/image.png)
![image](/uploads/d21cee4a3aec09bf754f83bb1081ce35/image.png)
* image는 issue에 클립보드 경로 복붙하고 링크 받아와서 걸어둔다

## docker 특징
    * vmware가 실행되어야 docker가 실행된다.
    * 근데 docker는 하이퍼v가 필요하고 vmware는 필요하지 않다.
    * 그래서 toolbox쓰는 것이다
    * docker는 리눅스 환경에서 쓰는게 좋다. window10에서는 지원해준다. 그래서 vmware가 필요없다.
### VM WARE
    * 그러나 대부분의 window10은 container가 필요하다.
    * 리눅스 명령어는 virture box에서 간단하게 쓰면 좋다.
    * point는 모든 기반은 unix이다.
    * right control은 마우스 오른쪽 + 아래
    * pwd 검색시 -> /home/docker


## 기술사 자격증 취득하기
    * 기술사가 있으면 경력으로 인정해서 연봉 책정된다.
    * 집중하면 따기 쉽다. 볼 수 있는 자격이 있다.

# docker 수업 1장 시스템과 인프라 기초 지식

### 시스템과 인프라 기초 지식
1. 서버
    * cpu
    * 메모리
    * 스토리지
2. 네트워크 주소
    * mac주소
    * ip주소 (IPv4를 많이 씀, 최근 IPv6 사용)
    [한국인터넷진흥원자료실](https://www.kisa.or.kr/public/laws/laws3.jsp)
### 하드웨어와 네트워크 기초 지식
1. OSI 참조 모델가 통신 프로토콜
    * tcp/ip 프로토콜(https://m.blog.naver.com/PostView.nhn?blogId=wnrjsxo&logNo=221184538679&proxyReferer=https:%2F%2Fwww.google.com%2F)
    ![image](/uploads/0dae251da806c18d0ef3e2ffc3cc4bde/image.png)
    * L7레이어 중요(시험 삘)

2. 방화벽
    * 보안 확보하기 위해 불필요한 통신 차단
3. 라우터/레이어 3스위치
    * 2개 이상의 서로 다른 네트워크 간을 중계하기 우한 통신 장비

### OS 기초 지식
![image](/uploads/db2972022aff15918cee80d91623612f/image.png)
    * SHELL : 리눅스 커넬 관리
        -사용자가 명령을 내려서 수행을 하기 위해서는 COMMAND가 필요한데, 해당 COMMAND의 모음을 SHELL이라고 한다.
    ![image](/uploads/8168dc73b34e1285093a0c65882cf262/image.png)
    * is-al치면 위 제품이 나온다.
    * 리눅스 용어의 신기함...다경언니 전공분야이다.bbbbb크~bbbbb
    * 
### 인프라 구성관리 기초 지식
* now infra is coding!!

    * 클라우드는 코딩을 통해 인프라를 구축한다.
    * 자도화 툴이 있기 때문에 이를 이용하여 가능하다.
    * kubernetes로 할 수 있다.

    1. 지속적 인티그레이션 : CI/CD
        * 애플리케이션의 코드를 추가/수정할때마다 테스트를 실행하고 확실하게 작동하는 코드를 유지하는 방법
        * DevOps dev가 coding을 통해 pipeline을 잘 해줘야한다.

# docker 수업 2장 컨테이너 기술과 Docker의 개요

### 컨테이너 기술의 개요
### docker의 개요
![image](/uploads/4c370b10c1b5490621d157f195ed1e2e/image.png)
* 모두 동일한 환경이 아닐 경우 힘들게 된다.
* 따라서 docker에 환경 세팅해서 해당 환경을 docker에 올린다.
* 이미지는 변경 불가능하다. -> immutable
    * 이미지가 바뀌면 이전 이미지 삭제하고 다시 올라간다.
    * 따라서 일정 시정 쓰지 않는 이미지는 날리는 작업이 필요하다
### docker의 기능
1. build
    * __docker 이미지를 만드는 기술__
    * docker는 애플리케이션의 실행에 필요한 프로그램 본체, 라이브러리, 미들웨어, os나 네트워크 설정 등을 하나로 모아서 docker이미지를 만듦
    * 도커 허브에서 한다
2. ship
    * __docker 이미지를 공유하는 기술__
    * docker 이미지는 docker 레지스트리에서 공유 가능
3. run
    * __dockr 이미지를 작동시키는 기능__
![image](/uploads/8ded5d5bac59e8d650d4c1191526c1f5/image.png)
    * dockr engine을 통해서 하게 될 것이다.

### docker의 작동 구조
1. namespace
* __namespace__
* 리눅스 기술의 기본 기술 중 하나.
* 이런 공간을 활용해 PID namespace, Network namespace, UID namespace, 등등의 기술 활용 -> 쿠버네틱스를 통해 사용됨

2. 릴리스 관리 장치(cgroups)
    * 프로세스와 스레드를 그룹화하여, 그 그룹 안에 존재하는 프로세스와 스레드에 대한 관리를 수행하기 위한 기능 계층 구조를 사용하여 프로세스를 그룹화하여 관리 가능. 

3. 네트워크 구성(가상 브리지/가상 NIC)
    * Linux는 Docker를 설치하면 서버의 물리 NIC가 docker0이라는 가상 브리지 네트워크로 연결. 

# 제 3장 Docker 설치와 튜토리얼
''' docker run hello-world'''
![image](/uploads/1c4067f364ad8df3dfe0503b88d3c8cc/image.png)
* 이렇게 적으면  .apk해서 sign을 받아옴 -> 반드시 식별자로 서명이 된 파일만 서비스한다,
* message digest : 해당되는 것으로 서명을 했는데 digest로 압축을 할때는 hash키로 압축한다.
* 즉 이미지 가져오려면 암호화해서 해야한당
![image](/uploads/f80b7fdb86a07da54a1292ec8d127d19/image.png)
- ㅎㅎㅎㅎ기욥당 git은 힘내~~~~

