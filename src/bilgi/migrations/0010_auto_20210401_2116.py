# Generated by Django 3.1.7 on 2021-04-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilgi', '0009_auto_20210401_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i̇nformationmodel',
            name='backimage',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='ana resim "1920-1100"'),
        ),
    ]