from django.db import models

# Create your models here.


class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.CharField(unique=True, max_length=255)
    card_security_code = models.CharField(max_length=3)
    card_issue_date = models.DateField()
    card_expiration_date = models.DateField()
    card_type = models.CharField(max_length=255)
    creditcard_brand = models.ForeignKey('MarcaTarjetas', models.DO_NOTHING)
    customer = models.ForeignKey('clientes.Cliente', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjeta'


class MarcaTarjetas(models.Model):
    creditcard_brand_id = models.IntegerField(primary_key=True)
    creditcard_brand_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'marca_tarjetas'
