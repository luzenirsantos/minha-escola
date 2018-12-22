from django.contrib import admin
from .models import *
from django.contrib.admin.options import InlineModelAdmin


class ProfessorAdmin(admin.ModelAdmin):
	list_display = ('matricula', 'nome', 'curso', 'turma')
	list_filter = ('nome', 'matricula', 'curso')

class CursoAdmin(admin.ModelAdmin):
	list_display = ('codigo_curso', 'nome', 'carga_horaria', 'valor')
	list_filter = ('codigo_curso','nome')

class ProfessorInline(admin.TabularInline):
    model = Professor

class TurmaAdmin(admin.ModelAdmin):
	inlines = [ProfessorInline]
	list_display = ('turma','curso','data_inicio', 'hora_inicio', 'hora_termino')
	list_filter = ('turma','curso')

admin.site.register(Curso, CursoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Recursos'
admin.site.site_title = 'Escola APROF' 
