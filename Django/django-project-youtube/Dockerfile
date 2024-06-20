# Python 3.11이 설치된 Alpine Linux 3.19
# Alpine Linux는 경량화된 리눅스 배포판으로, 컨테이너 환경에 적합
FROM python:3.11-alpine3.19

# LABEL 명령어는 이미지에 메타데이터를 추가합니다. 여기서는 이미지의 유지 관리자를 "seopftware"로 지정하고 있습니다.
LABEL maintainer="rbwo"

# 환경 변수 PYTHONUNBUFFERED를 1로 설정합니다. 
# 이는 Python이 표준 입출력 버퍼링을 비활성화하게 하여, 로그가 즉시 콘솔에 출력되게 합니다. 
# 이는 Docker 컨테이너에서 로그를 더 쉽게 볼 수 있게 합니다.
ENV PYTHONUNBUFFERED 1

# 로컬 파일 시스템의 requirements.txt 파일을 컨테이너의 /tmp/requirements.txt로 복사합니다. 
# 이 파일은 필요한 Python 패키지들을 명시합니다.
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000

# 개발환경인지 아닌지를 나타냄
ARG DEV=false
RUN apk add --update --no-cache libffi-dev
RUN python -m venv /py && \ 
    /py/bin/pip install --upgrade pip && \
    # 장고와 db를 연결하기 위한 커넥터를 설치해줌
    apk add --update --no-cache postgresql-client jpeg-dev && \
    # virtual 뒤 경로에 앞으로 설치할 패키지들을 저장하라는 명령어, &&를 작성하지 않아서 아래 두줄은
    # 한줄이라고 보면된다. &&: 엔터키라고보면댐
    apk add --update --no-cache --virtual .tmp-build-deps \
        # 아래 라이브러리들을 넘겨줌
        build-base postgresql-dev musl-dev zlib-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    # 항상 도커 컨테이너를 최적화하는게 중요하기 때문에 del 명령어도 작성해줌.
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    # 스크립트 실행 권한 부여
    chmod -R +x /scripts
    
    ENV PATH="/scripts:/py/bin:$PATH"
    USER django-user
    CMD ["run.sh"]