from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('capsules.urls')),
    path('', views.home_view)
]


