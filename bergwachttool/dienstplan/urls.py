from django.conf.urls import url

from . import views

app_name = 'dienstplan'

urlpatterns = [
    # ex: /dienstplan/
    url(r'^$', views.index, name='index'),
    url('dienst_overview/', views.dienst_list, name='dienst_list'),
    url('mitglieder_overview/', views.mitglieder_overview, name='mitglieder_overview'),
    url(r'^(?P<dienstnummer>[0-9]+)/$', views.dienst_detail, name='dienst_detail'),
    url(r'^mitglieder/(?P<username>[a-z]+)/$', views.mitglied_detail, name='mitglied_detail'),
    url(r'^anmeldung/(?P<dienstnummer>[0-9]+)/$', views.dienst_anmeldung, name='dienst_anmeldung'),
    url(r'^abmeldung/(?P<dienstnummer>[0-9]+)/(?P<username>[a-z]+)/$', views.dienst_abmeldung, name='dienst_abmeldung'),
]
