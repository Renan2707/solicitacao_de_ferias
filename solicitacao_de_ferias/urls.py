
from django.contrib import admin
from django.urls import path, include
from core.views.index import index, criar_user_rh

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('criar-user-rh', criar_user_rh, name='criar_user_rh'),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls')),
]
