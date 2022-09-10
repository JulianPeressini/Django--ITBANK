from django.db import models

# Create your models here.


class Cuenta(models.Model):
    account_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.CharField(max_length=100)
    account_type = models.ForeignKey(
        'TipoCuenta', models.CASCADE, blank=True)

    class Meta:
        managed = False
        db_table = 'cuenta'
        ordering = ['customer_id', ]

    def __str__(self):
        return str(self.customer_id) + ' (' + self.iban + ')'


class TipoCuenta(models.Model):
    account_type_id = models.IntegerField(primary_key=True)
    account_type_desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'

    def __str__(self):
        return self.account_type_desc
