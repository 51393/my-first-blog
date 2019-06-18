# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:19:42 2019

@author: kaoki
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]