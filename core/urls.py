from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from core import views


APPNAME = 'core'
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('', views.home, name="home"),
    path('catalogo/', views.CatalogoList.as_view(), name="catalogo"),
    path('catalogo/<int:pk>/', views.CatalogoDetail.as_view(), name="catalogo_detalhes"),
    path('cadastro/', views.CadastroList.as_view(), name="cadastro"),
    path('cadastro/<int:pk>/', views.CadastroDetail.as_view(), name="cadastro_detalhes"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
