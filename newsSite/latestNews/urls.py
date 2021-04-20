from django.urls import path

from . import views

app_name = 'newsSite'

urlpatterns = [
    path('', views.index, name='index'),
    path('latestNews/', views.stories, name='Latest News')
]
