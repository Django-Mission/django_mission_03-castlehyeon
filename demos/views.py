#http기능을 사용하기 위해 임포트
#from django.http import HttpResponse
#render를 쓰게 되면 코드가 간단
from django.shortcuts import render
#Random함수 임포트
#form random import random은 안되고, 그냥 import는 되네?
import random

def home(request):
        return render(request, 'index.html')

def input(request):
    return render(request, 'init.html')

def lotto(request):
    
    #1. 집합은 리스트와 달리 중복을 허용하지 않는다. (입력값 없음-로또번호 45개 저장)
    number = set()
    count = 0
    # 2. 계산
    # randint함수는 int(정수) 형으로 된 랜덤 한 값을 출력하는 함수
    #파라미터로 두가지 정수를 받으며, 각각 시작값과 끝값을 의미(포함)
    #집합에서 인자를 더하는 함수는 add, add에 randint를 넣어 1부터 45까지 랜덤한 정수가 나옴.
    # while문으로 number의 인수가 7개가 되게 반복
    while len(number) < 7: 
        number.add(random.randint(1, 45))

    #파이썬의 집합은 중복허용이 되지 않는 대신 순서가 없으므로, 숫자의 순서정렬을 위한 list자료형변환
    #list의 sort를 통해 순서대로 정렬
    number = list(number)
    number.sort()
    
    # 3. 응답
    #render 함수는 request와 템플릿명은 필수로 들어가며, html에 넘겨줄 변수를 적을 수 있다.
    #Django에서는 {{}}를 통해 템플릿 변수를 쓸 수 있다.
    return render(request, 'lotto.html', {'lottonumber': number})

