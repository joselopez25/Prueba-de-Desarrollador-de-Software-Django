# Generated by Django 5.0.4 on 2024-05-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_rename_user_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='libros_prestados',
            field=models.ManyToManyField(blank=True, null=True, related_name='usuarios_prestados', to='biblioteca.libro'),
        ),
    ]