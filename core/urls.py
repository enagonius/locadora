from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from core.views import login


APPNAME = 'core'
urlpatterns = [
    path('login/', login)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
