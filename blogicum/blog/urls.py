from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Подключаем URLs для блога
    path('pages/', include('pages.urls')),  # Подключаем URLs для страниц
    path('', views.index, name='index'),  # Главная страница
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)