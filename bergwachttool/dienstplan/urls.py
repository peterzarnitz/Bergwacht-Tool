from django.conf.urls import url

from . import views

app_name = 'dienstplan'

urlpatterns = [
    # ex: /dienstplan/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<dienstnummer>[0-9]+)/$', views.dienst_detail, name='dienst_detail'),
]
