# Flask 프로젝트

여러 질문들을 만들어서 질문 참여자의 결과 값을 통계로 보여주는 프로젝트

## 기능 분석 - routes

### def home()

앱을 처음 실행하면 동작하는 함수. GET 메소드로 해당 url로 들어오게된다면, `index.html`을 렌더링 하고 있다.

`index.html`에서는 참여자의 이름 나이 성별을 입력받아서 JSON 형태로 값을 전송한다.

### def add_participant()

`index.html`에서 참여자의 정보를 전송 받으면 실행되는 함수.

받은 값을 모델의 `Paticipant` 클래스에 맞게 값을 생성하여서 db에 저장한다.

리턴 값으로는 JSON 형태로 redirect 할 url(/quiz)값과, 참여자의 아이디 값을 반환한다.

이 JSON의 값들을 기준으로 `index.html`에서 참여자의 ID를 쿠키에 저장하고, 페이지를 이동시킨다.

### def quiz()

위에 함수에서 성공적으로 리다이렉션되면 실행되는 함수. 참여자의 아이디가 쿠키에 없다면 다시 처음페이지로 돌아간다.

DB에서 `Question` 값을 전부 들고와서 `questions` 변수에 할당하고, 질문의 콘텐츠들만 따로 배열로 만들어서 `quiz.html`을 렌더링할 때 값으로 전달해준다.

`quiz.html`에서는 `initializeQuiz()` 함수를 실행하는데 여기서는 먼저 `/questions`로 요청을 보낸다. 질문들이 보여지며, 모든 답변을 완료하면 질문의 결과값을 제출하게 된다. 제출 후에는 질문의 결과 값의 통계페이지로 이동된다.

### def questions()

위에 함수가 실행되면 바로 이 함수로 요청을 보내게 되는데, 이 함수는 DB의 Question 테이블의 값들을 가져오는데, 활성화된 질문의 경우에만 들고오고 JSON 형태로 바꿔서 반환해준다.

> quiz 함수에서도 질문들을 fetch 했었는데, 여기서 또 요청하고 있어서 하나의 함수에서만 요청을 하면 좀 더 효율적일듯하다

### def submit()

질문들의 결과를 제출하게 되면 실행되는 함수.

참여자ID를 먼저 검증하고, 받은 결과 값으로 `Quiz` 인스턴스를 생성하여 DB에 커밋한다.

반환 응답으로 리다이렉션할 URL과 메시지를 준다. 이때 `url_for("main.show_results")` 의 의미는 `main` 블루프린트 객체에 등록된 `show_results`의 url을 의미한다. 따라서 여기서는 `/results` 로 페이지 이동이 된다.

### def results()

결과값을 보여주는 페이지로 이동하면 실행되는 함수.

참여자와 퀴즈를 먼저 쿼리해온다음, pandas 데이터 형태에 맞게 변환해준다.

변환된 데이터를 그래프 데이터로 딕셔너리에 담아서 JSON 형태로 변환하여 `results.html`의 값으로 전달해준다.

### def login()

`/admin`로 이동하면 실행되는 함수. 

GET 메소드에서는 admin 계정을 로그인하는 `admin.html`을 렌더링하고있고, 아이디와 패스워드를 입력하여서 동일 URL로 POST 하면, 이 함수 내부에서 검증하고 admin 계정이 맞다면 세션에 로그인 상태라는 값을 True로 할당하고 `admin.dashboard` 함수에 맞는 URL로 리다이렉션한다.

#### next 파라미터 체크 코드 추가

밑에 로그인 체크하는 데코레이터 내부를 보면, url_for 에서 next 파라미터에 로그인 후, 다음 페이지로 이동될 url을 전달해주고 있다. 

하지만 기존 login 함수는 next 체크를 하고 있지 않았기 때문에, 원하는 동작이 이루어지지 않고 있어서 추가해주었다.

```html
<!-- admin.html -->
<form action="{{ url_for('admin.login', 
next = request.args.get('next')) }}" method="post">
```

```python
# routes.py
if request.method == "POST":
    ...
    next_url = request.args.get("next")
...
if next_url:
    redirect(url_for(next_url))
    
return redirect(url_for("admin.dashboard"))
```

### def login_required(f)

로그인 상태를 체크하는 데코레이터. 특정 함수를 받아서 로그인 체크 기능을 수행하고 다시 인자로 받은 함수를 반환해준다. 

이 과정에서 로그인이 안 되어 있다면은 로그인 페이지로 리다이렉션하고, `next` 파라미터에 로그인 후에 이동할 주소를 담아준다.

다음 이동할 주소에 변수가 있는 경우에는 아래 코드를 작성해주면 된다.

```python
query_string = urlencode(request.args)

return redirect(url_for('admin.login', next=f'{request.path}?{query_string}'))
```

### def dashboard()

참가자 수의 통계를 보여주는 동작을 하는 함수.

생성된 그래프를 `dashboard.html`로 전달해준다.

### def manage_questions()

질문을 관리하는 함수. 질문을 추가하거나 수정, 활성화의 기능을 한다.

GET, POST 메소드를 받고 있으며, 수정도 POST로 진행한다.

### def quiz_list()

DB에서 참여한 퀴즈의 결과 값을 전부 가져오는 함수. 

Quiz 테이블의 모든 로우를 가져와서 `quiz_list.html`에 전달해준다 
