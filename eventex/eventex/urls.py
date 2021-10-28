from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import home, speaker_detail


urlpatterns = [
    path('', home, name='home'),
    path('inscricao/', include('subscriptions.urls')),
    path(' palestrantes/<slug:slug>/', speaker_detail, name='speaker_detail'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )