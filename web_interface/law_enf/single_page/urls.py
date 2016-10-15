from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^add_query$', views.get_transcript)
]
