# Generated by Django 4.2.3 on 2023-07-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football_app', '0003_remove_stadiummodel_bron_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stadiummodel',
            name='address',
            field=models.TextField(default=''),
        ),
    ]
