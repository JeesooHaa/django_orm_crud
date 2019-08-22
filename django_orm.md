### Day01

언어 통합?

아무튼 세팅 바꾸면 다른 DB 다 쓸 수 있다. 



객체화를 시키겠다. 

객체지향적 데이터 접근 방식 



ORM - sql query / 근데 알아서 처리해줌 

우리는 class 처럼 사용하기만 하면되 



장점 : 엄청 쉽다 / 개발의 효율을 높일 수 있다 

단점 : 속도? / orm 이 제공하는 query 밖에 사용하지 못한다 



$ python manage.py makemigrations // django 한테 model 작성했음을 알림

$ python manage.py migrate // django 한테 실제 DB 에 작성하라고 명령 



### Day02

1. model 을 작성한다.
2. django 에 알려준다. makemigrations
3. 실제 DB 에 반영한다. migrate



django project 환경에서 python shell 을 사용한다.

```bash
$ python manage.py shell
```

article 을 import  해야 사용가능 

```shell
from articles.models import Article 
```

model 에 접근하는 명령어?

```python
<model>.objects
```

