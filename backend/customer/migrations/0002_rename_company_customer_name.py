# Generated by Django 4.2.2 on 2023-06-30 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='company',
            new_name='name',
        ),
    ]
