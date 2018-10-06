from django.contrib import admin
from django.conf.urls import include, url
from App import views

app_name = "App"
urlpatterns = [
    url(r'^$', views.index, name='Index'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.signout, name='logout')
]
