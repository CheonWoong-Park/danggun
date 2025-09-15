from django.db import models
import uuid

class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # 고유 ID
    name = models.CharField(max_length=50)  # 게시판 이름
    price = models.IntegerField()  # 가격
    serial = models.CharField(max_length=100)  # 제품 시리얼
    region = models.CharField(max_length=100)  # 지역
    seller = models.CharField(max_length=100)  # 판매자 이름
    article = models.TextField(max_length=10000)  # 게시판 내용
    date = models.DateTimeField(auto_now_add=True)  # 생성 시 자동으로 날짜 설정
