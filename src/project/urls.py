from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    pth('i18n/', include('django.conf.urls.i18n')),
    pth('admin/', admin.site.urls),
    # path('accounts/', include('accounts.site.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
