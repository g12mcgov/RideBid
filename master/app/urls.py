from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.conf.urls.defaults import patterns, url

import views
from models import Post

post_detail = DetailView.as_view(model=Post)
post_list = ListView.as_view(model=Post)

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^post/(?P<pk>[a-z\d]+)/$', post_detail, name='post_detail'),
    url(r'^$', post_list, name='post_list')
)