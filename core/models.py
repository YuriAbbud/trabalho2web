from django.db import models

class Cliente(models.Model):
    nome     = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=20)
    email    = models.EmailField()

    def __str__(self):
        return self.nome

class NotaFiscal(models.Model):
    ALIQUOTA_CHOICES = [
        (2, '2%'),
        (3, '3%'),
        (5, '5%'),
    ]

    cliente    = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='notas')
    descricao  = models.TextField()
    valor      = models.DecimalField(max_digits=10, decimal_places=2)
    aliquota   = models.IntegerField(choices=ALIQUOTA_CHOICES, default=3)
    iss        = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    valor_liq  = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    criado_em  = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.iss = float(self.valor) * float(self.aliquota) / 100
        self.valor_liq = float(self.valor) - self.iss
        super().save(*args, **kwargs)

    def __str__(self):
        return f'NF-{self.pk} | {self.cliente.nome}'
