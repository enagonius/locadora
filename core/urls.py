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
    path('catalogo/', views.FilmeList.as_view(), name="filme_list"),
    path('catalogo/<int:pk>/', views.FilmeDetail.as_view(), name="filme_detail"),
    path('catalogo/create/', views.FilmeCreate.as_view(), name='filme_create'),
    path('catalogo/<int:pk>/update/', views.FilmeUpdate.as_view(), name='filme_update'),
    path('catalogo/<int:pk>/delete/', views.FilmeDelete.as_view(), name='filme_delete'),
    path('cadastro/', views.ClienteList.as_view(), name="cliente_list"),
    path('cadastro/<int:pk>/', views.ClienteDetail.as_view(), name="cliente_detail"),
    path('cadastro/create/', views.ClienteCreate.as_view(), name='cliente_create'),
    path('cadastro/<int:pk>/update/', views.ClienteUpdate.as_view(), name='cliente_update'),
    path('cadastro/<int:pk>/delete/', views.ClienteDelete.as_view(), name='cliente_delete'),
    path('diretor/', views.DiretorList.as_view(), name="diretor_list"),
    path('diretor/<int:pk>/', views.DiretorDetail.as_view(), name="diretor_detail"),
    path('diretor/create/', views.DiretorCreate.as_view(), name='diretor_create'),
    path('diretor/<int:pk>/update/', views.DiretorUpdate.as_view(), name='diretor_update'),
    path('diretor/<int:pk>/delete/', views.DiretorDelete.as_view(), name='diretor_delete'),
    path('roteirista/', views.RoteiristaList.as_view(), name="roteirista_list"),
    path('roteirista/<int:pk>/', views.RoteiristaDetail.as_view(), name="roteirista_detail"),
    path('roteirista/create/', views.RoteiristaCreate.as_view(), name='roteirista_create'),
    path('roteirista/<int:pk>/update/', views.RoteiristaUpdate.as_view(), name='roteirista_update'),
    path('roteirista/<int:pk>/delete/', views.RoteiristaDelete.as_view(), name='roteirista_delete'),
    path('genero/', views.GeneroList.as_view(), name="genero_list"),
    path('genero/<str:pk>/', views.GeneroDetail.as_view(), name="genero_detail"),
    path('genero/create/', views.GeneroCreate.as_view(), name='genero_create'),
    path('genero/<str:pk>/update/', views.GeneroUpdate.as_view(), name='genero_update'),
    path('genero/<str:pk>/delete/', views.GeneroDelete.as_view(), name='genero_delete'),
    path('aluguel/', views.AluguelList.as_view(), name="aluguel_list"),
    path('aluguel/<int:pk>/', views.AluguelDetail.as_view(), name="aluguel_detail"),
    path('aluguel/create/', views.AluguelCreate.as_view(), name='aluguel_create'),
    path('aluguel/<int:pk>/update/', views.AluguelUpdate.as_view(), name='aluguel_update'),
    path('aluguel/<int:pk>/delete/', views.AluguelDelete.as_view(), name='aluguel_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
