from django.db import models
from django.utils import timezone


class Curso(models.Model):
	class Meta:
		verbose_name_plural="Cursos"

	codigo_curso = models.CharField('Código', max_length=5, unique=True)
	nome = models.CharField('Nome', max_length=20)
	ementa = models.TextField('Ementa')
	carga_horaria = models.IntegerField('Carga horária')
	valor = models.CharField('Valor', max_length=8)
	
	def __str__(self):
		return self.nome

class Turma(models.Model):
	turma = models.CharField('Turma', max_length=4)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	data_inicio = models.DateField('Data de início')
	hora_inicio = models.TimeField('Hora de início')
	hora_termino = models.TimeField('Hora de término')
	
	def __str__(self):
		return self.turma 

class Professor(models.Model):
	class Meta:
		verbose_name_plural="Professores"

	matricula = models.CharField('Matrícula', max_length=8, unique=True)
	nome = models.CharField('Nome', max_length=50)
	telefone = models.CharField('Telefone', max_length=11)
	email = models.EmailField('Email', max_length=100)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
	valor_hora = models.CharField('Valor da hora/aula', max_length=8)
	
	def __str__(self):
		return self.nome


		