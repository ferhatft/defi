# Generated by Django 3.1.7 on 2021-03-31 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilgi', '0006_remove_informationtextmodel_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informationtextmodel',
            old_name='dictionary',
            new_name='information',
        ),
    ]
