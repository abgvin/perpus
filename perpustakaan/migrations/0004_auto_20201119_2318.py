# Generated by Django 2.2.12 on 2020-11-19 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0003_auto_20201119_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelompok',
            name='keterangan',
            field=models.TextField(null=True),
        ),
    ]
