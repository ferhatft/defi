# Generated by Django 3.1.7 on 2021-04-19 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20210405_0146'),
        ('haber', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerinlineModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True, verbose_name='Öne çıkarma')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('main_context', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_owner', to='profiles.userprofile', verbose_name='Görüş Sahibi')),
                ('information', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='NewsModelAnswer', to='haber.newsmodel')),
            ],
            options={
                'verbose_name': 'Cevap',
                'verbose_name_plural': 'Cevaplar',
                'ordering': ['created_date'],
            },
        ),
    ]
