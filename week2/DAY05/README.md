# SK infosec 클라우드 AI 전문가 양성과정

## WEEK 02
### 07/17


* 위 설치를 위해서는 2가지 방법이 있다.
1. __간단한 Dockerfile을 작성하여 dockerfile이 실행될때 run에 install 내용을 추가하는 것__



2. __github에 올려진 내용 복붙하는 법__
- 강사님은 이것을 더 추천하셨다.
***

## centos위에 maria DB 시작
* MariaDB는 오픈 소스의 관계형 데이터베이스 관리 시스템(__RDBMS__)이다. 
    - 1) googleing 및 복사
    - ![image](/uploads/7cc17caae9be5a5ae666ee177e3ac5e4/image.png)
    - 검색창에 centos dockerfile github로 검색한다
    - dockerfile 내용을 찾아서 복사 붙여넣기 한다.
    - 귀찮으면 그냥 그대로 다운받아서 폴더에 복붙하면 된다.
    - 2) 이미지 제작한다
## centos 위에 mariadb 설치하기
## cetos_mariadb.zip download 압축풀기
<pre>
<code>    
~\centos_mariadb>docker build -t ai/mariadb55:1
docker images //확인
</pre>
</code>
#container 생성
<pre>
<code>
docker run --name=mariadb -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password ai/mariadb55:1
docker ps
docker exec -it mariadb bash
@bash$mysql -u root -p
Enter Password : password
mysql>show databases;    //mysql shell에서 databases 확인
mysql>use mysql;         //mysql db 사용
mysql>quit;              //mysql shell 종료
@bash$exit;              //bash shell 종료
</pre>
</code>


## centos위에 mongo DB 시작
* MongoDB는 Document-Oriented(문서 지향적) __NoSQL__ 데이터베이스이다. 
    - #centos base image에 mongodb 설치하기
#cetos_mongodb.zip download 압축풀기
<pre>
<code>
~\centos_mogndb>docker build -t ai/mongodb:1 .
</pre>
</code>
#container 생성
<pre>
<code>
docker run --name=mongodb -d -p 27017:27017 ai/mongodb:1
docker ps
dcoker exec -it mongodb bash
@root#ls -al  //data/db 폴더확인
@root#ls -al /user/bin/mongod 확인
</pre>
</code>


# 제 3부 실행환경 구축
## 클라우드를 사용한 docker 실행 환경 구축

* 클라우드 환경에서 docker 오케스트레이션 하기
    #### 구글 cloud활용 kubernetes engines 사용하기
    * __google cloud platform의 컨테이너 관련 서비스__
        - google container builder
        - google kubernetes engine
        - googke containter registry
    * __kubernetes의 개요__
    - kubernetes : 쿠버네티스는 서로 연결되어서 단일 유닛처럼 동작하는 고가용성의 컴퓨터 클러스터를 상호조정한다
    - 쿠버네티스는 애플리케이션 컨테이너를 클러스터에 분산시키고 스케줄링하는 일을 보다 효율적으로 자동화한다.
        - ![image](/uploads/12fe3d40d71c9f1b4324a69793e975e8/image.png)
        - ![image](/uploads/328cec87872fbfcf7f6b511fa62f4a45/image.png)
        - 쿠버네티스는 기본적으로 노드로 관리를 해준다.
        - 노드에는 마스터/work로 나눠진다.
        - 노드 내 점선 박스를 pod라고 하는데 이 pod 내 사각형을 컨테이너라고 한다.
        - 컨테이너 관리(컨테이너의 집합) = pod
        - 1개 이상 pod 관리 = node : 애플리케이션을 구동하는 작업자
        - 일반 work 노드의 관리 = 마스터 node : 클러스터를 상호조정한다.
        - node의 역할 = gateway
        - 즉 각각의 파드(pod)들이 게이트웨이를 통해 들어가게 된다.
        - 리플리카셋 : 클러스터 상에서 미리 지정된 pod를 작성하여 실행시켜 두는 장치
        - ReplicaSet은 실행중인 POD를 감시하여 장애와 같은 이슈로 정지된 경우에 해당 POD를 삭제하고, 새로운 POD를 실행시킨다.  
        - *POD와 리플리카에 대한 개념은 꼭 잡기* 
        
    * __중요__ ++ 컨테이너는 독립적이라서 자료 공유가 안된다.
    >   > - 따라서 똑같은 형태의 pod가 각각의 노드에 있다고 하더라도, 별도의 컨테이너가 설치될 필요성이 있다.
    * 구글 cloud 컨테이너 관리
        - ![image](/uploads/3090336d095b53a0bf44726b2f37300c/image.png)
        - 클러스터 기본 사항 적고 노드에 부팅 디스크 크기와 노드당 최대 pod수 찾기
        - question ! 노드 __풀__ 풀을 쓰는 이유는 ? 
        > 노드 풀은 클러스터 내에서 구성이 모두 동일한 노드 그룹
        > 인스턴스가 많으면 퍼포먼스가 떨어진다. 그래서 인스턴스를 삭제하게 되는데, 그렇게 되는 경우 효율이 떨어진다. 따라서 인스턴스 1개를 생성하는 대신 풀 인스턴스를 제작하게 되는 것이다. 대규모이기 때문에 로드하는데 시간이 걸리지만 풀에서 가져가서 서비스 하게 하면 더 효율적이다. 따라서 pool에서 해당 모듈을 쓰고 다 쓴 경우 반납을 하게 된다. 
        > 예를들어 100명에게 각각의 인스턴스 100개 생성하는 것보다 인스턴스 풀 4개를 만들어서 100명에게 서비스하는게 더 효율적이라는 것이다. 공유하는 데이터가 없다면 전~혀 문제가 되지 않는다.

    * 클러스터 생성 
    - ![image](/uploads/319de08a9cf91cd4d8f31db7de4a8d12/image.png)
    - 클러스터 생성 파일
    * compute engine -> vm 인스턴스
    - 생성된 3개의 클러스터가 확인 가능하다.
    - 생성된 3개의 클러스터는 노드로 이해하고, masternode는 우리에게 오픈할 필요가 없다. 따라서 우리가 워커 노드 3개에 하면 된다.    
    * 노드의 구성
    - ![image](/uploads/ada57e97886cd44f6cd660f62a03d395/image.png)
    - 해당 페이지는 compute engine > vm 인스턴스
    - 노드 > pod > 컨테이너
    * 쿠퍼네틱스 오프라인
    - [관련문서](https://cloud.google.com/sdk/install?hl=ko)
    - 구글 sdk(명령줄 인터페이스)를 사용할 수도 있다. 이것을 사용하기 위해서는 아래 vscode의 확장팩을 사용하면 쉽다.   
    - ![image](/uploads/cbd935f82cc21d0f0633ded1a4dc72e8/image.png)
    - 상황이 여의치 않을 경우에 cloud에서 제공하는 shell을 활용하면 좋다.
    - ![image](/uploads/7508c55aea27d9f548de019d63c1b41d/image.png)
    - 이름의 gcloud 대화형 셀 사용하면 된다. [관련문서](https://cloud.google.com/sdk/docs/scripting-gcloud?hl=ko)


* kubernetes 
+ ```kubectl get nodes```
    - : kuber네틱스의 nodes확인
+ ``` kubectl get nodes -o wide```
    - : 쿠버네틱스의 노드 한개의 상세 정보를 확인할 수 있다.
+ yaml파일이 있다면 yaml파일을 이용해 인스턴스를 생성함
+ yaml파일이 없으니 직접 쉘에 다음을 입력
    - ```kubectl create deployment hello-server -image=gcr.io/google-samples/helloapp:1.0```
    - ```kubectl get pods ``` : 실행중인 pod 검사
    - ```kubectl get service hello-server``` : 서비스 검사
    - ![image](/uploads/682bba054bb2556d23978f58c85d5203/image.png)
    - 이렇게 하면 3개의 클러스터 중 한개를 찾을 수 있다. 
    - 근데 curl해도 방화벽때문에 안된다. 
    - ![image](/uploads/6b854287577eaa3592394776437277e6/image.png)
    - vpc 네트워크 < 방화벽 규칙 만들기 < 이름 정하고, 대상태그, 소스 ip범위 등등 채워넣기
    - 이미지 삭제법 -> 작업 부하에 들어가서 클러스터 삭제하기
    - 해당 클러스터 상세보기 중에서 노출중인 서비스의 엔드포인트 찾아서 ip주소 확인하기
    - ```curl 34.71.68.177``` : 해당 호스팅 주소 확인하기
    ### 정리
    * [gke빠른시작](https://cloud.google.com/kubernetes-engine/docs/quickstart?hl=ko)
    <pre>
    <code>   
    kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0
    kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0
    kubectl get pods   
    kubectl describe services hello-server
    curl 34.71.68.177
    </pre>
    </code>
    ***
    * 도커파일로 실행하기 
    - dockerfile에 다음과 같은 내용 붙여넣기
    <pre>
    <code>
    FROM golang:1.8-alpine
    ADD . /go/src/hello-app
    RUN go install hello-app

    FROM alpine:latest
    COPY --from=0 /go/bin/hello-app .
    ENV PORT 8080
    CMD ["./hello-app"]
    </pre>
    </code>
    
    ***


