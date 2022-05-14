#demos/urls.py

from django.urls import path
from .views import lotto, home, input
#from polls.views import *

urlpatterns = [
   path('init', input, name='input'),
   path('init/lotto', lotto, name='result'),
   path('', home, name='home'), 
    #path('', IndexView.as_view(), name='polls'), #127.0.0.1:8000/polls/
    #path('test/', TestView.as_view(), name='polls_test'), #127.0.0.1:8000/polls/test/
]