from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil, Convite, Postagem
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import *


@login_required
def index(request):
	return render(request, 'index.html', {'perfis': Perfil.objects.all(),
										  'perfil_logado': get_perfil_logado(request)})


@login_required
def exibir(request, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	ja_eh_contato = perfil in perfil_logado.contatos.all()
	return render(request, 'perfil.html', {'perfil': perfil, 'perfil_logado': get_perfil_logado(request),
										   'ja_eh_contato': ja_eh_contato})


@login_required
def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)

	return redirect('index');


@login_required
def get_perfil_logado(request):
	return request.user.perfil


@login_required
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

@login_required
def bloquear_usuario(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    request.user.perfil.bloquear(perfil)
    return redirect('index')

@login_required
def desbloquear_usuario(request,perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    request.user.perfil.desbloquear(perfil)
    return redirect('index')

@login_required
def desfazer(request,perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	perfil.desfazer(get_perfil_logado(request))
	return redirect('index')



@login_required
def postagem(request):
	postagens = [post for post in request.user.perfil.perfil_postagens.all()]
	usuario = request.user.perfil
	print(postagens)
	contatos = request.user.perfil.contatos.all()
	for contato in contatos:
		for post in contato.perfil_postagens.all():
			postagens.append(post)

	return render(request, 'postagens.html', {'posts': postagens, 'usuarioLogado': usuario})


def add_post(request):
	if request.method == 'POST':
		postform = PostForm(request.POST or None)
		if postform.is_valid():
			postin = postform.save(commit=False)
			postin.usuario = request.user.perfil
			postin.save()
			return redirect('index')
	else:
		postform = PostForm()
	return render(request, 'add_postagem.html', {'post': postform})

@login_required
def deletar_postagem(request,id_post):
    Postagem.objects.filter(id=id_post).delete()
    return redirect('index')