# Generated by Django 4.2.2 on 2023-06-30 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_plan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='max_clients',
            new_name='max_customers',
        ),
    ]