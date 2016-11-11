from django.conf.urls import url
from polls import views

urlpatterns = [

    # Example: /polls/
    url(r'^$', views.index, name='index'),
    # Example: /polls/1/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # Example: /polls/1/vote
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    # Example: /polls/1/result
    url(r'^(?P<question_id>\d+)/result/$', views.result, name='result'),
]
