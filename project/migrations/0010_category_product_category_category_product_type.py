# Generated by Django 4.1.5 on 2023-03-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_category_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='product_category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='category',
            name='product_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]
