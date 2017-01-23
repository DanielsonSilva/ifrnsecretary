# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
from __future__ import unicode_literals

from django.db import models

# PROFESSORES
class Professor(models.Model):
	idprofessor = models.AutoField(primary_key=True)
	matricula = models.CharField(unique=True, max_length=30)
	nome = models.CharField(max_length=150)
	email = models.EmailField(max_length=50, blank=True)

# TURMAS
class Turmas(models.Model):
	idturma = models.AutoField(primary_key=True)
	codigo = models.CharField(max_length=20)
	
# DISCIPLINAS
class Disciplinas(models.Model):
	iddisciplina = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=200)
	
# CURSO
class Curso(models.Model):
	idcurso = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=250)
	
# ALUNO
class Aluno(models.Model):
	idaluno = models.AutoField(primary_key=True)
	matricula = models.CharField(unique=True, max_length=30)
	nome = models.CharField(max_length=150)
	idcurso = models.ForeignKey(Curso, on_delete=models.PROTECT)
	idturma = models.ForeignKey(Turmas, on_delete=models.PROTECT)
	contato = models.CharField(max_length=20, blank=True)
	email = models.EmailField(max_length=50, blank=True)
	
# ATIVIDADES
class Atividades(models.Model):
	idatividade = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=50)
	
# DOCUMENTOS
class Documentos(models.Model):
	iddocumento = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=50)

# REQUERIMENTOS
class Requerimentos(models.Model):
	idrequerimento = models.AutoField(primary_key=True)
	idaluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
	data = models.DateField(auto_now=True)
	posicao = models.CharField(max_length=300, blank=True)
	status = models.IntegerField()
	responsavel = models.ForeignKey(Professor, on_delete=models.PROTECT)
	
# REPOSIÇÕES
class Reposicoes(models.Model):
	idreposicao = models.AutoField(primary_key=True)
	idrequerimento = models.ForeignKey(Requerimentos, on_delete=models.PROTECT)
	data = models.DateField()
	idatividade = models.ForeignKey(Atividades, on_delete=models.PROTECT)
	idprofessor = models.ForeignKey(Professor, on_delete=models.PROTECT)
	justificativa = models.CharField(max_length=300)
	iddocumento = models.ForeignKey(Documentos, on_delete=models.PROTECT)
	arquivo = models.FileField(upload_to='seacpar/%Y/%m/')


	
