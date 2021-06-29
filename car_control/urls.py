from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:mat>/', views.DetailView.as_view(), name='detail'),
]