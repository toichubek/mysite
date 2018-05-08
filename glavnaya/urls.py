# -*- coding: utf-8 -*-

from django.urls import path, include
from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('', views.index, name='index'),
    path('news.html', views.news, name='news'),
    path('<int:News_id>', views.new, name='new'),
    path('contacts.html', views.contacts, name='contacts'),
    path('istoria.html', views.istoria, name='istoria'),
    path('polozheniye.html', views.polozheniye, name='polozheniye'),
    path('team.html', views.team, name='team'),
    path('kursy.html', views.kursy, name='kursy'),
    path('faq.html', views.faq, name='faq'),
    path('photogallery.html', views.photogallery, name='photogallery'),

]
