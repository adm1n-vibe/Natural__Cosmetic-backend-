# Generated by Django 5.0.2 on 2024-03-02 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Products', 'verbose_name_plural': 'Products'},
        ),
    ]