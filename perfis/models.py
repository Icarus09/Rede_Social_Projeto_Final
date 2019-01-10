from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=20, null= False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('Perfil')
    bloqueados = models.ManyToManyField('Perfil', related_name='contatos_bloqueados')
    usuario = models.OneToOneField(User, related_name="perfil", on_delete=models.CASCADE, default="", editable=False)


    def __str__(self):
        return self.nome

    @property
    def email(self):
        return self.usuario.email

    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self,convidado = perfil_convidado)
        convite.save()

    def bloquear(self, perfil):
        self.bloqueados.add(perfil)
        self.desfazer(perfil)
        self.save()

    def desbloquear(self, perfil):
        self.bloqueados.remove(perfil)
        self.convidar(perfil)
        self.save()

    def desfazer(self, perfil):
        self.contatos.remove(perfil)
        perfil.contatos.remove(self)

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='convites_feitos' )
    convidado = models.ForeignKey(Perfil, on_delete= models.CASCADE, related_name='convites_recebidos')

    def aceitar(self):
        self.solicitante.contatos.add(self.convidado)
        self.convidado.contatos.add(self.solicitante)
        self.delete()

class Postagem(models.Model):
        texto = models.CharField(max_length=140)
        data = models.DateTimeField(default=timezone.now)
        usuario = models.ForeignKey(Perfil, related_name='perfil_postagens', on_delete=models.CASCADE)
