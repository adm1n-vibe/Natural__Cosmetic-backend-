# Generated by Django 5.0.2 on 2024-02-27 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
    ]
