from django.urls import path

from .views import QuizList, QuizDetail
from .views import ResultDetail

urlpatterns = [
    path('quiz/', QuizList.as_view(), name='quiz_list'),
    path('quiz/<slug:slug>/result', ResultDetail, name='result_detail'),
    path('quiz/<slug:slug>', QuizDetail, name='quiz_detail'),
]
