# Generated by Django 3.1.4 on 2020-12-30 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number',
            field=models.CharField(max_length=10),
        ),
    ]