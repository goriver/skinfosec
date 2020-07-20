# SK infosec 클라우드 AI 전문가 양성과정

## WEEK 03
### 07/20

# DB[데이터베이스 철저공략]
* 학습목표
    1.  __PYTHON에서 데이터를 RDBMS에 저장하기__
    2. __도커에서 다운받은 MONGO DB 이미지를 이용하여 실습__
    3. __NOSQL을 활용하여 JSON형태로 데이터 저장하기__

### RDBMS
<pre>
* 정보보안 분석론에 따른 목차
    1. 요구사항 분석
    2. 개념적 데이터 모델링 
    3. 상세 개념적 데이터 모델링
    4. 논리적 데이터 모델링
    5. 물리적 설계
</pre>

### 요구사항 분석
* 정보 요구사항의 중요성
    - 잘못된 정보 요구사항으로 분석, 설계된 시스템을 개발한다면 사용자의 요구사항을 만족하지 못하게 될 것
    - 비용과 시간을 재투자해야하는 문제 발생
* 요구사항 발생 흐름
    - 요구사항 정의서, 명세서
        - 1) application 설계 ->  n.f
            - architecture 설계서
        - 2) 분석 설계 -> f
            - ui분석 | 설계 (화면 명세서.화면설계서)
            - 객체분석 | 설계
            - db분석 | 설계

* 정보 요구사항 관리
    - 1) 정보 요구사항 수집
    - 2) 정보 요구사항 분석/정의
    - 3) 정보 요구사항 상세화
    - 4) 정보 요구사항 검증

* 요구사항 분석 - 정보 요구사항 수집 절차
    
![image](/uploads/fc1f560bdbf76f2f7bae8d34a7de4f7c/image.png)


* __*6W3H에 의한 엔티티명의 분류*__
- ![image](/uploads/7b0bbf5bec2ed15c4fd3e5f6a4396184/image.png)
- 6하원칙에 맞춰서 위와 같이 뽑아내라는 것 
- ![image](/uploads/9b1d1e8a1eb71de0ad87b50247d2c859/image.png)
- 궁극적으로는 업무에서 쓰는 용어를 그대로 코드에 적용하는 것이 바람직하다.

* 데이터 명칭 
    - 카멜케이스 적용 X , 소문자 + _ 로 적어라
    
* __엔티티(Entity)__
    - 정의 : 최소한의 정보단위
    - 데이터의 집합을 의미한다.
    - 저장되고, 관리되어야하는 데이터이다.
    - 개념, 장소, 사건 등을 가리킨다.
    - 유형 또는 무형의 대상을 가리킨다.

### 개념적 데이터 모델링
* __모델링(Modeling)__
    - 정의 : 데이터 모델링은 복잡한 현실 세계를 단순화시켜 표현하는 것이다.
    - 데이터 모델링은 개념 데이터 모델링, 논리 데이터 모델링, 물리 데이터 모델링의 단계가 있다.
    - 구축 < 구현이 정확한 표현이다.

* __개념적데이터모델링(ISP)__
    - 정의 : 실 세계의 현상을 알기 쉽고 체계적으로 모형화 해 놓은 것
    - 조달 단계에 위치함
    - ISP내 용어 이해
    - 관계를 표현하는데는 여러가지 방법이 있다.
    - 하나의 부서는 반드시 하나의 지역에 속해있다. OR-> OPTIONAL로 표현

* __용어이해__
    - ![image](/uploads/bef2a8ebbaad9b33162a64a4ac2efe69/image.png)
    - entitiy : 기업에서 지속적인 관심을 가지고 정보화해야하는 대상
    - attribute : entity를 구성하는 고유한 정보들
    - uid : unique identifier
    - relationship : 객체 간의 직접적인 관계, 각 entity 간의 업무적 상관관계를 도식화 한 것

*Entity의 개념*
![image](/uploads/c18b88e6b144b95a5602f7daf8e428ab/image.png)

* ENTITY 추출
    1. 명사로 된 단어 찾기
    2. 비즈니스 분석내용 중에서 찾기
    3. 명사로 된 단어 중에 같은 의미로 사용되면서 다르게 표현되는 단어는 제외
    4. 속성으로 표현되는 단어는 제외하고 어떤 ENTITY에 포함되는지 파악
    + 다른 수 있기때문에 OR MAPPING하기 / 또는 1:1로 매핑해도 됨   
    + 그러나 1:1로 매핑하면 재사용을 못함.   

* Attribute 추출
    - ENTITY 내에서 관리해야 할 정보들의 항목으로 최소단위까지 분할함
    - 정보 항목의 최소 단위이어야 하며 업무적 성격에 따라 단어가 독자적인 성질을 가질 수 있어야 함
    - 유추 가능한 속성은 제외

* UID 추출
    - 여러 개의 속성 중에 ENTITY를 대표할 수 있는 속성을 찾음
    - 여러 개의 속성이 결합되어 하나의 식별자가 될 수도 있음

* Relationship 정의
    - Relationship이란 객체 간의 직접적인 관계를 의미하며 간접적인 관계는 배제
    - 각 ENTITY간의 업무적 상관관계를 도식화 한 것
    - 실체화 실체 간에 중복되는 속성을 가졌으면 RELATION이 될 수 있음
    - 실세계에서 사용되는 동사적 단어들이 RELATION이 될 수 있다.
    - 멀티플러스피가 설정되어야지 타입이 결정될 수 있다. 
    - 따라서 RELATIONSHIP을 넣을 때도 __샘플 데이터를 하나 넣으면 된다.__
    - 데이터 샘플로 집어넣으면 조금 더 명확하다.
***
* __ERD 작성__
- 기업마다 다른 배치도 형식을 가진다. PDF는 BARKER이고, 교과서는 IDEF1X를 사용한다. 
    - ![image](/uploads/a3989fc02199d11c6a19af42dd239c3f/image.png)
    - 다음과 같은 이미지를 많이 보고 작성해라.
    - ERD(Entity-Relation Diagram) : 개체 관계도
    - 현실 세계에 존재하는 데이터와 그들 간의 관계를 사람이 이해할 수 있는 형태로 명확하게 표현하기 위해서 가장 널리 사용되고 있는 모델
    - *새발 표기법*
        - <img src="/uploads/a6af47a6ef5a500a962f335eb86fa5a3/image.png" width = "60%"></img>
        - <img src="/uploads/c622c58dbc09525f86507f131bb050f6/image.png" width = "60%"></img>
        - [BARKER을 활용한 ERD블로그](https://dlgkstjq623.tistory.com/319)
           *시험 삘 예를 들어서 그림 주고 해석하라는 식* 

### 상세 개념적 데이터 모델링

* __개요__
    - 개념적 모델링이 실세계 현상을 표현했다면, 상세 개념적 모델링은 보다 명확하게 ENTITY를 표현하고 ATTRIBUTE를 제거, 추가하는 과정
    - 즉 정규화는 ENTITY를 검증한다고 이해한다.

* __정규화 필요이유__
    1. 데이터 중복성 제거
    2. 데이터 모형을 단순화
    3. ATTRIBUTE의 배열 상태를 검증
    4. ENTITY, ATTRIBUTE의 누락여부를 검증
    5. 데이터 모형의 안정성을 유지

* 정규화의 장/단점
    - <img src="/uploads/5c4d2ee9a4b43c369506d70e81e2735a/image.png" width = "60%"></img>
    - [제N정규화](https://myeonguni.tistory.com/210)
    - 가장 쉽게 이해하는 법 : SAMPLE DATA를 넣어보기
    1. 제 1정규화
        - ENTITY내에 모든 속성은 반드시 하나의 값을 가져야 함
        - <img src="/uploads/2a151d60f64a14655dd69cca76114571/image.png" width = "60%"></img>
        - <img src="/uploads/abb906050f7923df25accc5754fa83cb/image.png" width = "60%"></img>
        - 자격증 데이터를 따로 분류하여 정규화를 진행한다. 
        - 왜냐하면 각각 하나의 값을 가지고 있는데 자격증이고, 나머지는 중복되기 때문이다.
    2. 제 2정규화
        - COMPOSITE KEY의 경우 ENTITY내의 모든 속성은 반드시 COMPOSEITE KEY에 종속 되어야 함
        - 주식별자가 아닌 속성들 중에서 주실별자 전체가 아닌 일부 속성에서 종속된 속성을 찾아 제거
        - <img src="/uploads/d83caf10cff7cb46537d8568961e33dd/image.png" width = "60%"></img>
        - <img src="/uploads/377f42e4e4b8df74e25a2748ae392674/image.png" width = "60%"></img>
        - 해결책은 COMPOSITE KEY로 참조하도록 하면 된다!
        - 
    3. 제 3정규화
        - 주식별자가 아닌 속성들 중에서 종속관계에 있는 속성을 찾아 제거하는 과정  
        - 제 2정규화와 헷갈리면 ㄴㄴ
        - 주식별자가 아닌 속성들 중에서 종속 관계에 있는 속성을 찾아 제거
        - <img src="/uploads/2306a11e132dff66839266239d1ef724/image.png" width = "60%"></img>
        - <img src="/uploads/95b6d6d0640d9175f32af5f1357510c3/image.png" width = "60%"></img>

### 논리적 데이터 모델링

* __개념__
    - 개념적 모델링 과정을 통해 만들어진 개념적 구조들을 DBMS가 처리할 수 있는 객체로 생성하는 과정
    - <img src ="/uploads/831702719ccfe4c6e277dd24e86b9cd8/image.png" width = "60%"></img>
    - ENTITY -> TABLE
    - ATTRIBUTE -> COLUMN
    - IDENTIFIER -> PRIMARY-KEY
    - RELATION -> FOREIGN-KEY

* __논리적 데이터의 RDBMS개요__
    * DATABASE
        - 한 조직의 여러 응용 시스템에서 공용할 수 있도록 중복되는 데이터를 최소화하여 통합/저장한 운영 데이터 집합을 의미
    * DBMS(DataBase Management System)
        - 데이터베이스에서 데이터를 저장.검색.수정하는 데이터베이스 전용 관리 프로그램
    * RDBMS(Relational DataBase Management System)
        - 모든 데이터를 2차원 테이블 형태로 표현하고 테이블 사이의 비즈니스 광계에 도추하는 구조를 가진 데이터베이스 유형

    * *software*
    - [차이점url](https://m.blog.naver.com/PostView.nhn?blogId=xodltus&logNo=220583633081&proxyReferer=https:%2F%2Fwww.google.com%2F)
        - mysqldb
            : sql 문장 사용
        - mongodb 
            : 몽고 쿼리 문장 사용

* __주요용어__
    - ![image](/uploads/85d47d952d952111b48f30c609f13f03/image.png)
    - ![image](/uploads/27671a9db7d92948c199715f761ea772/image.png)
        * __candidate key [후보키]__ : candidate key는 relation을 구성하는 attribute들 중에서 tuple을 유일하게 식별하기 위해 사용하는 attribute의 부분집합을 말한다.
        * __primary key [기본키]__ : 후보키에서 선택되어 사용되는 main key이다. NULL 값을 가질 수 없으며 기본키로 정의된 attribute에는 중복된 값이 올 수 없다.
        * __alternate key [대체키]__ : 후보키중에서 기본키를 제외한 나머지 키들을 말한다.
        * __super key [슈퍼키]__ : 한 relation에 있는 attribute의 집합으로 구성된 key로 relation을 구성하는 모든 tuple 중 슈퍼키로 구성된 attribute의 집합과 동일한 값은 나타나지 않는다.
        * __foreign key [외래키]__ : Relationship을 맺고 있는 R1,R2가 있다고 하자. 이 때 R1이 R2의 기본키를 참조하고 있으면 기본키를 참조할 때 기준이 되는 Key 값이 R1에 존재하는데 이를 외래키라고 한다. 외래키로 지정되면 참조 relation의 기본키에 없는 값은 입력할 수 없다.

* __DATABASE의 데이터 타입__
    - <img src ="/uploads/4d87356b8045ac293bd810ad8d62ec30/image.png" width = "60%"></img>

### 물리적 설계
* __물리적 설계의 개요__
    - <img src ="/uploads/76bf2e12b29fa4d04fa86636ea1c79d9/image.png" width = "60%"></img>
    - 최종 설계된 ERD모델에 대해 테이블의 물리적 저장구조에 대한 설계를 한 후 스키마 생성
    ***
    - ![image](/uploads/99e5fd0922793388af4f8d1ce15895a6/image.png)
    - [SQL언어 종류 참고 링크](https://m.blog.naver.com/PostView.nhn?blogId=liccorob&logNo=10152844072&proxyReferer=https:%2F%2Fwww.google.com%2F)
    - 쿼리 연습 특히 DQL로 하면 좋다.
    - ![image](/uploads/60f0cfda91b930caaa8ebadc28c16074/image.png)