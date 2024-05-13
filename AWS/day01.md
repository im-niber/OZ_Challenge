## 클라우드, AWS

### 클라우드 컴퓨팅 개념

클라우드 컴퓨팅이란 인터넷 기반 컴퓨팅의 일종으로 정보를 자신의 컴퓨터가 아닌 크라우드에 연결된 다른 컴퓨터로 처리하는 기술을 의미한다.

클라우드 컴퓨팅은 컴퓨팅 리소스를 인터넷을 통해 서비스로 사용할 수 있는 서비스이다. 일반적으로는 인터넷 기반 컴퓨팅의 일종으로 정보를 자신의 컴퓨터가 아닌 클라우드에 연결된 다른 컴퓨터로 처리하는 기술을 의미함.

### 리전, 가용영역, 엣지 로케이션

- 리전: 가용영역이 2개 이상 구성된 지리적 영역. 일종의 클러스터처럼 묶여있으며 많은 서비스들이 리전을 기반으로 해서 제공됩니다. 리전 내의 가용영역 간에는 높은 대역폭과 지연시간이 짧은 네트워크로 연결되어, 빠른 서비스로 응답을 제공할 수 있습니다.
- 가용영역: 1개 이상의 물리 데이터센터를 묶은 논리적인 데이터센터. 1개의 데이터센터일 수도 있고, 2개 이상의 데이터센터를 묶어놓은 것일 수도 있습니다. 가용영역 간에는 물리적으로 떨어져있기 때문에 데이터센터의 장애가 발생하더라도 영향을 미치지 않습니다.
- 엣지로케이션: 아마존의 CDN 서비스인 `CloudFront`를 위한 캐시 서버들의 모음을 의미함.

### 클라우드 종류

- IaaS 서비스형 인프라스트럭처: 가상머신과 기타 컴퓨팅 자원들을 구독자에 대한 서비스로 제공하는 모델. 물리적 컴퓨팅 자원, 위치, 데이터파이셔닝, 확장 보안 백업과 같은 인프라의 세세한 부분을 제공해준다. EC2가 대표적인 예시이다.
- PaaS 서비스형 플랫폼: 개발자들에게 개발 환경을 제공하는 모델, 일반적으로 개발을 위한 도구와 표준 그리고 배포 및 지불을 위한 채널을 개발한다. 클라우드 제공자는 일반적으로 OS, 언어실행환경, DB, 서버를 포함한 플랫폼을 제공한다. 구글의 App엔진, Heroku 등이 대표적인 예시이다.
- SaaS 서비스형 소프트웨어: 클라우드 제공자는 프로그램을 실행하는 구조와, 플랫폼을 관리한다. 주문형 소프트웨어(on-demand software)를 가리키기도 한다. 클라우드에 응용 소프트웨어를 설치, 운영하며 사용자들은 클라우드 클라이언트의 소프트웨어를 접근한다. 사용자는 클라우드 구조와 플랫폼을 관리하지 않는다. 대표예시로는 네이버 클라우드, 드롭박스 등이 있다. 

### EC2

생성 

![1](/images/aws_images/day01/1.png)

접속 

![2](/images/aws_images/day01/2.png)

보안그룹 

![3](/images/aws_images/day01/3.png)

### ElasticIP

생성 

![4](/images/aws_images/day01/4.png)

할당 

![5](/images/aws_images/day01/5.png)

접속 

![6](/images/aws_images/day01/6.png)

해제 

![7](/images/aws_images/day01/7.png)