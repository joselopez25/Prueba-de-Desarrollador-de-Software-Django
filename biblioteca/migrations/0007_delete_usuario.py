# Generated by Django 5.0.4 on 2024-05-07 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_alter_users_libros_prestados'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]