# Generated by Django 3.1.7 on 2021-04-19 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haber', '0002_answerinlinemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answerinlinemodel',
            old_name='information',
            new_name='news',
        ),
    ]
