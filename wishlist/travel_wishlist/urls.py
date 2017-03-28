from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.place_list, name='place_list'),
    url(r'^city/(?P<pk>\d+)/$', views.place_detail, name='place_detail'),

    url(r'^city/(?P<pk>\d+)/edit/$', views.place_edit, name='place_edit'),

]
