from django.contrib import admin
from confeitaria.models import *

# Register your models here.
class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(Produto, Produtos)

class Problemas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tipo')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(Problema, Problemas)

class FuncoesObjetivas(admin.ModelAdmin):
    list_display = ('id', 'problema')
    list_per_page = 20

admin.site.register(Funcao_Objetiva, FuncoesObjetivas)

class Restricoes(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', 'descricao')
    list_per_page = 20
    search_fields = ('descricao',)

admin.site.register(Restricao, Restricoes)

class Restricoes_Coeficientes(admin.ModelAdmin):
    list_display = ('id' ,'restricao', 'coeficiente')
    list_display_links = ('id',)

admin.site.register(Restricao_Coeficiente, Restricoes_Coeficientes)

class Resultados_Problemas(admin.ModelAdmin):
    list_display = ('id','problema','status', 'valor_otimo', 'data_calculo')
    list_display_links = ('id',)

admin.site.register(Resultado_Problema, Resultados_Problemas)

class Resultados_Variaveis(admin.ModelAdmin):
    list_display = ('id','resultado', 'produto', 'valor')
    list_display_links = ('id',)

admin.site.register(Resultado_Variavel, Resultados_Variaveis)