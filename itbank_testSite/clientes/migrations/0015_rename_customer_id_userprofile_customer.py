# Generated by Django 4.1 on 2022-09-07 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0014_alter_userprofile_customer_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='customer_id',
            new_name='customer',
        ),
    ]
