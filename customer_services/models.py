from csv import writer
from tkinter import CASCADE
from unicodedata import category
from django.db import models
#django에서 제공하는 user테이블을 가져오기 위해
from django.contrib.auth import get_user_model

#유저 테이블 함수 호출
User = get_user_model()


#FAQ 모델 생성
class Faq(models.Model):
    #질문 제목
    title = models.CharField(max_length=100)
    #질문-글 내용은 양이 많으므로 TextField,필수
    question = models.TextField(verbose_name='질문내용') 
    #카테고리, choices 사용 //일반, 계정, 기타
    #개발할 때 이해하기 쉽게, 상수로 선언
    NOMAL = 'NO'
    ACCOUNT = 'AC'
    MISCELLANEOUS = 'MISC'
    CATEGORY_CHOICES = [
        (NOMAL, 'NO'),
        (ACCOUNT, 'AC'),
        ( MISCELLANEOUS, 'MISC'),
        ]
    #카테고리 모델
    category = models.CharField(
        max_length=4,
        choices=CATEGORY_CHOICES,
        default=NOMAL,
    )    
    
    #답변
    comment = models.TextField(verbose_name='답변내용') 
    #생성일시. 게시 시간 로그, 필수, auto_속성값을 추가, 처음 생성 시, 필드를 현재로 설정.
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    #게시글과 댓글은 모두 작성자가 들어감. //null은 실제로 DB에 null값을 허용하는가. blank도 유효성 검사에서 값이 없어도 허용할 것인가에 대해 명시.
    
    #작성자가 foreignkey로 묶여있는 것은 콤보박스로 들어간다.
    created_by = models.ForeignKey(User, related_name='작성자', on_delete=models.CASCADE)
    #auto_now : 생성 및 수정 시 업데이트.
    #auto_now_add : 생성 시에만 업데이트
    
    #조회수, 필수, default값은 0이다.
    view_count = models.IntegerField(verbose_name='조회수', default=0)

    #최종 수정자
    modified_by = models.ForeignKey(User, related_name='수정자', on_delete=models.CASCADE)
    
    #최종 수정일시. 저장할 때마다 현재를 설정
    modified_at = models.DateTimeField(verbose_name='수정일', auto_now=True)

#Mission3
class Inquiry(models.Model):
        
    #질문 제목
    title = models.CharField(max_length=100)

    #카테고리
    NOMAL = 'NO'
    ACCOUNT = 'AC'
    MISCELLANEOUS = 'MISC'
    CATEGORY_CHOICES = [
    (NOMAL, 'NO'),
    (ACCOUNT, 'AC'),
    ( MISCELLANEOUS, 'MISC'),
    ]

    #카테고리 모델
    category = models.CharField(
        max_length=4,
        choices=CATEGORY_CHOICES,
        default=NOMAL,
    )  

    # 이메일(올바른 형식인지 판별하는 기능 구현: 간단하게. @가 들어갔나.)
    email = models.EmailField(max_length=200, verbose_name="이메일")
        
    # 전화번호(최대 11자리)
    phone = models.CharField(max_length = 11, verbose_name="전화번호")
        
    #작성일시
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
        
    #작성자(최종수정자는 필요없지 않을까?)
    created_by = models.ForeignKey(User, verbose_name='질문작성자', on_delete=models.CASCADE)
        
    #내용
    content = models.TextField(verbose_name='내용')

# 답변(Answer)
class Answer(models.Model):
        
    #답변내용
    coment = models.TextField(verbose_name="답변내용")

    #운영자(related_name이 faq와 같은 경우 reverse accessor 에러메세지)
    created_by = models.ForeignKey(User, related_name='답변작성자', on_delete=models.CASCADE, null=True, blank=True)

    #생성일시
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")

    #질문과 관계를 맺어줘야해서 새로 ForeinKey필드를 만들어야함.
    inquiry = models.ForeignKey(to='Inquiry', on_delete=models.CASCADE, null=True, blank=True)