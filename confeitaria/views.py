from django.shortcuts import render
from confeitaria.models import *
from rest_framework.decorators import action
from rest_framework.response import Response
from confeitaria.serializer import *
from rest_framework import viewsets, generics
from pulp import *

# Create your views here.
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProblemaViewSet(viewsets.ModelViewSet):
    queryset = Problema.objects.all()
    serializer_class = ProblemaSerializer

class Funcao_ObjetivaViewSet(viewsets.ModelViewSet):
    queryset = Funcao_Objetiva.objects.all()
    serializer_class = Funcao_ObjetivaSerializer

class RestricaoViewSet(viewsets.ModelViewSet):
    queryset = Restricao.objects.all()
    serializer_class = RestricaoSerializer

class Restricao_CoeficienteViewSet(viewsets.ModelViewSet):
    queryset = Restricao_Coeficiente.objects.all()
    serializer_class = Restricao_CoeficienteSerializer

class Resultado_ProblemaViewSet(viewsets.ModelViewSet):
    queryset = Resultado_Problema.objects.all()
    serializer_class = Resultado_ProblemaSerializer

class Resultado_VariavelViewSet(viewsets.ModelViewSet):
    queryset = Resultado_Variavel.objects.all()
    serializer_class = Resultado_VariavelSerializer

class Problema_CompletoViewSet(generics.ListAPIView):
    def get_queryset(self):
       return Problema.objects.filter(id=self.kwargs['pk'])
    serializer_class = Problema_CompletoSerializer

class CalcularSimplex(viewsets.ModelViewSet):
    """
    Endpoint para resolver o problema de Programação Linear (Simplex)
    com base nas tabelas do banco.
    """

    @action(detail=True, methods=["get"])
    def resolver(self, request, pk=None):
        try:
            problema = Problema.objects.get(pk=pk)
            produtos = Produto.objects.all()
            funcoes_objetivas = Funcao_Objetiva.objects.filter(problema=problema)
            restricoes = Restricao.objects.filter(problema=problema)

            # Cria modelo
            modelo = LpProblem(
                problema.nome,
                LpMaximize if problema.tipo == "maximizar" else LpMinimize
            )

            # Cria variáveis
            variaveis = {p.id: LpVariable(p.nome, lowBound=0) for p in produtos}

            # Função objetivo
            modelo += lpSum([
                float(fo.coeficiente) * variaveis[fo.produto.id]
                for fo in funcoes_objetivas
            ])

            # Adiciona restrições
            for r in restricoes:
                coeficientes = Restricao_Coeficiente.objects.filter(restricao=r)
                lhs = lpSum([
                    float(c.coeficiente) * variaveis[c.produto.id]
                    for c in coeficientes
                ])

                if r.sinal == "<=":
                    modelo += lhs <= float(r.limite)
                elif r.sinal == ">=":
                    modelo += lhs >= float(r.limite)
                else:
                    modelo += lhs == float(r.limite)

            # Resolve o problema
            modelo.solve()

            resultado = {
                "status": LpStatus[modelo.status],
                "valor_otimo": value(modelo.objective),
                "variaveis": {v.name: v.varValue for v in modelo.variables()}
            }

            # Salvar resultado no banco
            resultado_model = Resultado_Problema.objects.create(
                problema=problema,
                status=resultado["status"],
                valor_otimo=resultado["valor_otimo"]
            )

            for nome_variavel, valor in resultado["variaveis"].items():
                produto = Produto.objects.filter(nome=nome_variavel).first()
                if produto:
                    Resultado_Variavel.objects.create(
                        resultado=resultado_model,
                        produto=produto,
                        valor=Decimal(str(valor))
                    )

            return Response({"status": "success", "resultado": resultado})

        except Exception as e:
            return Response({"erro": str(e)}, status=400)