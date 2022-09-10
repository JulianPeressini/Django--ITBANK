from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    employee_surname = models.CharField(max_length=255)
    employee_hire_date = models.CharField(max_length=255)
    employee_dni = models.CharField(max_length=255)
    branch_id = models.IntegerField()
    direccion = models.ForeignKey(
        'clientes.Direccion', models.CASCADE, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'

    def __str__(self):
        return self.employee_name + ' ' + self.employee_surname + ' (' + str(self.employee_id) + ')'
