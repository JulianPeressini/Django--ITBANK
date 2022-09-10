from django.db import models


class Sucursal(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    branch_number = models.IntegerField()
    branch_name = models.CharField(max_length=255)
    branch_address_id = models.IntegerField()
    direccion = models.ForeignKey(
        'clientes.Direccion', models.CASCADE, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'
