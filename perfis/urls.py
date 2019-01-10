from django.urls import include, path
from perfis import views

urlpatterns = (
	path('', views.index, name='index'),
	path('perfil/<int:perfil_id>', views.exibir, name='exibir'),
	path('perfil/<int:perfil_id>/convidar', views.convidar, name='convidar'),
	path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar'),
	path('<int:perfil_id>/bloquear', views.bloquear_usuario, name='bloquear'),
	path('<int:perfil_id>/desbloquear', views.desbloquear_usuario, name='desbloquear'),

)