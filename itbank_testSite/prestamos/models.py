from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Prestamo(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    loan_type = models.CharField(max_length=20)
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'

    def __str__(self):
        return 'Prestamo: ' + str(self.loan_id) + ' (' + str(self.customer_id) + ')'
