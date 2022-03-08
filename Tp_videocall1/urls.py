from django.contrib import admin
from . import  settings
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from agora.views import Agora
from App.models import Channel


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("App.urls")),
    path('agora/',Agora.as_view(
        app_id='',
        channel=''
    )),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
