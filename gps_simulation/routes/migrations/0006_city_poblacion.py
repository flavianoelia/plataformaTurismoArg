# Generated by Django 5.1.1 on 2024-11-08 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0005_alter_city_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='poblacion',
            field=models.TextField(null=True),
        ),
    ]
