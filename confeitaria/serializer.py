from rest_framework import serializers
from confeitaria.models import *

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
    
class ProblemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problema
        fields = "__all__"

class Funcao_ObjetivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao_Objetiva
        fields = "__all__"

class RestricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restricao
        fields = "__all__"

class Restricao_CoeficienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restricao_Coeficiente
        fields = "__all__"

class Resultado_ProblemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado_Problema
        fields = "__all__"

class Resultado_VariavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado_Variavel
        fields = "__all__"

class Problema_CompletoSerializer(serializers.ModelSerializer):
    # Produtos únicos usados no problema
    produtos = serializers.SerializerMethodField()

    # Função objetiva
    funcao_objetiva = serializers.SerializerMethodField()

    # Restrições
    restricoes = serializers.SerializerMethodField()

    # Resultado
    resultados = serializers.SerializerMethodField()

    class Meta:
        model = Problema
        fields = "__all__"
    
    def get_produtos(self, obj):
        produtos = Produto.objects.filter(funcao_objetiva__problema=obj).distinct()
        return ProdutoSerializer(produtos, many=True).data

    def get_funcao_objetiva(self, obj):
        funcoes = Funcao_Objetiva.objects.filter(problema=obj)
        return Funcao_ObjetivaSerializer(funcoes, many=True).data

    def get_restricoes(self, obj):
        restricoes = Restricao.objects.filter(problema=obj)
        return RestricaoSerializer(restricoes, many=True).data

    def get_resultados(self, obj):
        resultados = Resultado_Problema.objects.filter(problema=obj).order_by('-data_calculo')
        return Resultado_ProblemaSerializer(resultados, many=True).data