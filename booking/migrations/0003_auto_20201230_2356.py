# Generated by Django 3.1.4 on 2020-12-30 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20201230_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number',
            field=models.CharField(max_length=15),
        ),
    ]
