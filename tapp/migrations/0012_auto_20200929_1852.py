# Generated by Django 3.1.1 on 2020-09-29 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0011_auto_20200928_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]