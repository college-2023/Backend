# Generated by Django 4.1.5 on 2023-03-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='product_name',
            field=models.CharField(default='название продукта', max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='product_price',
            field=models.IntegerField(default='цена продукта(сом)'),
        ),
    ]
