# -*- coding: utf-8 -*-


from django.conf.urls import url,include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('wiki', views.WikiView)
routers.register('wikicount', views.WikiCountView)

urlpatterns = [
    url('', include(routers.urls)),
]
