from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('/.well-known/change-password', RedirectView.as_view(url='password_change')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
