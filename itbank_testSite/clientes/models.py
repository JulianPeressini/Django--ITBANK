from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_surname = models.CharField(max_length=255)
    customer_dni = models.CharField(db_column='customer_DNI', max_length=255)
    dob = models.CharField(blank=True, null=True, max_length=255)
    branch_id = models.IntegerField()
    direccion = models.ForeignKey(
        'Direccion', models.CASCADE, null=True)
    client_type = models.ForeignKey(
        'TipoCliente', on_delete=models.CASCADE, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return self.customer_name + ' ' + self.customer_surname + ' (' + str(self.customer_id) + ')'


class TipoCliente(models.Model):
    client_type_id = models.IntegerField(primary_key=True, blank=True)
    client_type_desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'

    def __str__(self):
        return self.client_type_desc


class Direccion(models.Model):
    direccion_id = models.IntegerField(primary_key=True)
    dir_calle = models.CharField(max_length=255)
    dir_city = models.CharField(max_length=255)
    dir_province = models.CharField(max_length=255)
    dir_country = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'direccion'

    def __str__(self):
        return self.dir_city + ', ' + self.dir_calle
