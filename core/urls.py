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
    path('catalogo/<int:pk>/', views.CatalogoDetail.as_view(), name="cliente_detail"),
    path('catalogo/create/', views.CatalogoCreate.as_view(), name='filme_create'),
    path('catalogo/<int:pk>/update/', views.CatalogoUpdate.as_view(), name='filme_update'),
    path('catalogo/<int:pk>/delete/', views.CatalogoDelete.as_view(), name='filme_delete'),
    path('cadastro/', views.CadastroList.as_view(), name="cadastro"),
    path('cadastro/<int:pk>/', views.CadastroDetail.as_view(), name="filme_detail"),
    path('cadastro/create/', views.CadastroCreate.as_view(), name='filme_create'),
    path('cadastro/<int:pk>/update/', views.CadastroUpdate.as_view(), name='cliente_update'),
    path('cadastro/<int:pk>/delete/', views.CadastroDelete.as_view(), name='cliente_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
