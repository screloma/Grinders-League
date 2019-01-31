from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', auth_views.login, {'template_name': 'login.html'}),
    path('main/', views.index, name='index'),
    path('addUser/', views.addUser, name='addUser'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
