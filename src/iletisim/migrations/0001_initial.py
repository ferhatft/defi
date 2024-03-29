# Generated by Django 3.1.7 on 2021-05-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=25, null=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('read', 'Read'), ('closed', 'Closed')], default='new', max_length=6)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Mesaj',
                'verbose_name_plural': 'Mesajlar',
                'ordering': ['name'],
            },
        ),
    ]
