from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'), # Executes method views.index
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'), # Angle brackets indicate question_id is input to views.detail
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]