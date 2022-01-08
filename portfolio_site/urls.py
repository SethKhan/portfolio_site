from django.urls import path
from quote_generator import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
]
