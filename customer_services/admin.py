from telnetlib import STATUS
from django.contrib import admin
#Post 모델을 임포트, admin과 같은 경로 상에 있기 때문에 .models
from .models import Faq, Inquiry, Answer
#TabularInline, StackedInline 어떻게 배치할 것인가의 차이, 1:n의 관계일 때, n을 어떻게 할 것인지.

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    #(괄호 안에는 모델의 속성명을 넣어주는 것.)
    #불필요한 정보는 안보여주고, 답변내용이 아닌 답변여부로 수정
    list_display = ('title', 'category', 'modified_at', 'view_count')
    #list_editable = ('content') -> 리스트 화면에서 수정이 바로 가능하다.
    list_filter = ('category',)
    #튜플형태 () 와 리스트형태 [] 는 다르다. 튜플형태일 때 마지막에 콤마를 넣어야한다.
    search_fields = ('title', )
    #작성자를 넣게 된다면... lgitookup
    #search_fields = ('id', 'writer__username') 언더바_ *2
    search_help_text = '제목 검색이 가능합니다.'
    #readonly속성을 줌으로써, post내부에 게시날짜가 보이게 함.
    readonly_fields = ('created_at', )

    #admin에서 중요한 기능인, actions를 정의해보자.
    actions = ['make_published']

    #인자값으로 받은 세개의 정보
    def make_published(modeladmin, request, queryset):
        #admin action에 대한 결과가 queryset에 들어온다.
        for item in queryset:
            item.title='운영 규정 위반으로 인한 게시글 삭제 처리.'
            item.save()

        #queryset.update(status='p')


#인라인으로 사용할 답변 클래스 생성
class AnswerInline(admin.TabularInline):
    model = Answer
    verbose_name = '답변'
    verbose_name_plural = '답변'


@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    # category의 참조에러메시지 -> category 모델정의를 안하고 상수선언만 했기 때문에
    list_display = ('title', 'category', 'created_at', 'created_by')
    
    #카테고리 필터
    list_filter = ('category',)
    
    #검색 필드
    search_fields = ('title', 'email', 'phone', )
    
    #검색어에 대한 설명
    search_help_text = '제목, 이메일, 전화번호 검색이 가능합니다.'

    #인라인요소로 들어갈 Answer
    inlines = [AnswerInline]


#조회수가 많은 순서대로 Faq를 보여주면 좋을 것.
#카테고리 모델이 각 클래스에서 겹치기 때문에 models.py에서 별도 모델을 만들어 클래스에서 호출할 수 있게는 할 수 없을까?
#(admin.E202) 'customer_services.Answer' has no ForeignKey to 'customer_services.Inquiry'. -> 관계를 맺어줄 수 있는 필드 선언으로 해결
#It is impossible to add a non-nullable field 'inquiry' to answer without specifying a default. -> 디폴트값을 넣어주니 해결
#답변하는 관리자와 일반사용자의 권한을 다르게 주고 사용해보았으면 한다. // 사용자는 답변할 수 없고, 질문만.