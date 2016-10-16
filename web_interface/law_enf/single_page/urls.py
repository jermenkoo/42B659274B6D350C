from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^add_query$', views.get_transcript),
    url(r'^decrypt_phone', views.decrypt)
]
