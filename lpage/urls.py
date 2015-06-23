from django.conf.urls import patterns, url, include
from lpage import views

urlpatterns = patterns('',
	url(r'^send-message/', views.send_message),
	url(r'^4pet', views.index),
)