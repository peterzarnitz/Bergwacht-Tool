from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /dienstplan/
    url(r'^$', views.index, name='index'),
]
