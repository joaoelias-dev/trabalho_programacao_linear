from django.contrib import admin
from django.urls import path, include
from confeitaria.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produtos', ProdutoViewSet)
router.register('problemas', ProblemaViewSet)
router.register('funcoes-objetivas', Funcao_ObjetivaViewSet)
router.register('restricoes', RestricaoViewSet)
router.register('restricoes-coeficientes', Resultado_ProblemaViewSet)
router.register('resultados-problemas', Restricao_CoeficienteViewSet)
router.register('resultados-variaveis', Resultado_VariavelViewSet)
#router.register('calcular-simplex', CalcularSimplex)

urlpatterns = [
    path('', include(router.urls)),
    path('calcular-simplex/<int:pk>/', CalcularSimplex.as_view({'get':'resolver'})),
    path('problemas/<int:pk>/completo', Problema_CompletoViewSet.as_view()),
]
