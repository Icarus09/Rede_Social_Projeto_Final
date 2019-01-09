from django.urls import path
from django.contrib.auth import views as v
from usuarios.views import RegistrarUsuarioView

urlpatterns =[
	path('registrar/', RegistrarUsuarioView.as_view(), name="registrar"),
	path('login/', v.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', v.LogoutView.as_view(template_name='login.html'), name='logout')
]