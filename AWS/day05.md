- 과제 1) IAM
    - IAM 사용자 생성하기
    ![1](/images/aws_images/day05/1.png)
    - 생성한 IAM 사용자로 AWS 콘솔 로그인하기
    ![2](/images/aws_images/day05/2.png)
    - EC2 페이지 접속하여 잘 나오는지 확인하기
    ![3](/images/aws_images/day05/3.png)
    - IAM 사용자 삭제하기
    ![4](/images/aws_images/day05/4.png)

- 과제 2) AWS SDK, CLI 공유자격 증명 설정
    - IAM 사용자 생성하기 (S3ReadOnlyAccess 권한 포함)
    ![16](/images/aws_images/day05/16.png)

    - 생성한 IAM 사용자에 액세스 키 만들기
    ![17](/images/aws_images/day05/17.png)

    - 생성한 액세스 키를 사용하여 사용 중인 컴퓨터에 공유 자격 증명 설정하기
    ![18](/images/aws_images/day05/18.png)

    - AWS CLI를 사용하여 S3 명령어 테스트하기
    ![19](/images/aws_images/day05/19.png)

    - IAM 사용자 삭제하기
    ![21](/images/aws_images/day05/20.png)


- 과제 3) DynamoDB 
    - 스키마 설계 후 DynamoDB 테이블 생성하기
    ![5](/images/aws_images/day05/5.png)
    - 보조 인덱스 (글로벌) 생성하기
    ![6](/images/aws_images/day05/6.png)
    - 생성한 테이블에 항목을 몇 개 생성하기, 이때 자유롭게 속성도 추가하기
    ![8](/images/aws_images/day05/8.png)
    - 항목 쿼리한 결과를 캡쳐하기, 글로벌 보조 인덱스를 사용하여 쿼리하기
    ![9](/images/aws_images/day05/9.png)
    
    ![10](/images/aws_images/day05/10.png)

    - 항목 스캔한 결과를 캡쳐하기
    
    ![11](/images/aws_images/day05/11.png)

    - 테이블 삭제하기
    
    ![12](/images/aws_images/day05/12.png)


- 과제 4) AWS Lambda
    - 블루프린트를 사용하여 함수를 하나 생성하기 (Hello world function)
    ![13](/images/aws_images/day05/13.png)
    - 테스트 이벤트 구성하고 테스트 실행해보기
    ![14](/images/aws_images/day05/14.png)
    - 람다함수 삭제하기
    ![15](/images/aws_images/day05/15.png)