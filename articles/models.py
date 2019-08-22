from django.db import models


class Article(models.Model):
    # id(pk)는 기본적으로 처음 테이블 생성시 자동으로 만들어 진다.
    # 따라서 만들 필요가 없음...
    # id = models.AutoField(primary_key=True) 

    # 모든 필드는 기본저으로 NOT NULL => 비어있으면 안된다. 
    
    # CharField 에서는 max_length 가 필수 인자다. 
    title = models.CharField(max_length=20)  # 클래스 변수 (DB의 필드)
    content = models.TextField()  # 클래스 변수 (DB의 필드)
    created_at = models.DateTimeField(auto_now_add=True)  # add 추가됬을때
    updated_at = models.DateTimeField(auto_now=True)  # 수정되었을때 (언제든지)

    def __str__(self):
        return f'{self.id}번 글 - {self.title} : {self.content}'
                