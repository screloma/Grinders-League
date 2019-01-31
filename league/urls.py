from django.contrib import admin
from django.urls import path, include
from login import views as core_views
urlpatterns = [
    path('', include("login.urls")),
    path('register/', core_views.signup, name="signup"),
    path('admin/', admin.site.urls),
]
