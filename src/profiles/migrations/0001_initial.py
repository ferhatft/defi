# Generated by Django 3.1.7 on 2021-03-17 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abaout', models.TextField(verbose_name='Hakkında')),
                ('profileimage', models.ImageField(upload_to='', verbose_name='Profil Resmi')),
                ('usertype', models.CharField(choices=[('freelancer', 'Freelancer'), ('ofis', 'Ofis'), ('hizmet_alan', 'Hizmet_alan')], default='hizmet_alan', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Tam İsim')),
            ],
        ),
    ]