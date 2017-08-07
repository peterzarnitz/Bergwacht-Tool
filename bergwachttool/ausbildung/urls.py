from django.conf.urls import url

from . import views

app_name = 'ausbildung'

urlpatterns = [
    # ex: /dienstplan/
    url(r'^$', views.index, name='index'),
]
