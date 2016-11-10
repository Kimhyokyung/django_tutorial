from django.conf.urls import url
from polls import views

urlpatterns = url[
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='result'),
    url(r'^(?P<queestion_id>\d+)/vote/%', views.vote, name='vote')
]

