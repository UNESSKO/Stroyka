# Generated by Django 4.1.7 on 2023-03-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gagaga',
            name='img',
            field=models.ImageField(upload_to='main/static/src/media', verbose_name='Изображение'),
        ),
    ]