from django.urls import path
from . import views

#Маршруты для «О нас», «Правила» и др.

app_name = 'pages'  # Указываем namespace для приложения

urlpatterns = [
    path('about/', views.about, name='about'),  # Страница "about"
    path('rules/', views.rules, name='rules'),  # Страница "rules"
]
