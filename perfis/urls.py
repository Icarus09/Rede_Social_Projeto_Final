from django.urls import include, path
from perfis import views

urlpatterns = (
	path('', views.index, name='index'),
	path('perfil/<int:perfil_id>', views.exibir, name='exibir'),
	path('perfil/<int:perfil_id>/convidar', views.convidar, name='convidar'),
	path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar'),
)