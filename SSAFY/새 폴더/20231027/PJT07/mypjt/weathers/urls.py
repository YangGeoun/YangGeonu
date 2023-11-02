from django.urls import path
from . import views

urlpatterns = [
    # 1. 날씨 API 테스트
    # 2. 서울의 5일치 예보 데이터 화인
    # 3. 예보 데이터 중 원하는 데이터만 DB에 저장
    # 4. 저장한 데이터 전체 조회
    # 5. 특정 조건 데이터 확인 : 섭씨 30도가 넘는 시간대 조회
    path('', views.index),
]
