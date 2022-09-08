from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    # Field name made lowercase.
    customer_dni = models.TextField(db_column='customer_DNI')
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    direccion = models.ForeignKey(
        'Direccion', models.CASCADE, null=True)
    # This field type is a guess.
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
    direccion_id = models.AutoField(primary_key=True)
    dir_calle = models.TextField()
    dir_city = models.TextField()
    dir_province = models.TextField()
    dir_country = models.TextField()

    class Meta:
        managed = False
        db_table = 'direccion'

    def __str__(self):
        return self.dir_city + ', ' + self.dir_calle
