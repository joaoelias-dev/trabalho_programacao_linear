from django.db import models
from decimal import Decimal

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.nome

class Problema(models.Model):
    nome = models.CharField(max_length=255, blank=False)
    TIPO_OBJETIVO = [("maximizar","maximizar"),("minimizar","minimizar"),]
    tipo = models.CharField(max_length=10, choices=TIPO_OBJETIVO, default="maximizar")
    descricao = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    
class Funcao_Objetiva(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    problema = models.ForeignKey(Problema, on_delete=models.CASCADE)
    coeficiente = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

class Restricao(models.Model):
    problema = models.ForeignKey(Problema, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255, blank=False)
    sinal = models.CharField(max_length=3, blank=False, choices=[("<=", "<="), (">=", ">="), ("=", "=")])
    limite = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

    def __str__(self):
        return self.descricao
    
class Restricao_Coeficiente(models.Model):
    restricao = models.ForeignKey(Restricao, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    coeficiente = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

class Resultado_Problema(models.Model):
    problema = models.ForeignKey(Problema, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    valor_otimo = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))
    data_calculo = models.DateTimeField(auto_now_add=True)

class Resultado_Variavel(models.Model):
    resultado = models.ForeignKey(Resultado_Problema, on_delete=models.CASCADE, related_name="variaveis")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

