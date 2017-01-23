# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# USUÁRIOS
class Usuarios (models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	matricula = models.CharField(max_length=20)
	foto = models.ImageField(upload_to='profile/',null=True)	
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Usuarios.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.usuarios.save()