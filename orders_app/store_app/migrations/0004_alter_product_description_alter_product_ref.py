# Generated by Django 4.1 on 2022-09-16 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0003_product_description_product_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='ref',
            field=models.CharField(max_length=100),
        ),
    ]
