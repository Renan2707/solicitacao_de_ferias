
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views.index import index, criar_user_rh

urlpatterns = [
    path('admin-django-solicitacao-ferias-macrosul/', admin.site.urls),
    # path('criar-user-rh', criar_user_rh, name='criar_user_rh'),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
