from django.contrib import admin
from django.conf.urls import include, url
from App import views

app_name = "App"
urlpatterns = [
    url(r'^home/', views.index, name='Index')
]
