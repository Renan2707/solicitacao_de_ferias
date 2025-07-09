
from django.contrib import admin
from django.urls import path, include
from core.views.index import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('allauth.urls')),
]
