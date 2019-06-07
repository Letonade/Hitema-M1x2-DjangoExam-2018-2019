from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accueil', views.home),
    path('core/', include('core.urls')),
]