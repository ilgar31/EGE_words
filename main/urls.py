from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path("words/all", views.all_words, name='all_words'),
    path("words/noun", views.noun_words, name='noun_words'),
    path("words/adjective", views.adjective_words, name='adjective_words'),
    path("words/verbs", views.verbs_words, name='verbs_words'),
    path("words/communion", views.communion_words, name='communion_words'),
    path("words/adverbs", views.adverbs_words, name='adverbs_words'),
    path("words/gerunds", views.gerunds_words, name='gerunds_words'),
    path("words", views.words, name='words')
]
