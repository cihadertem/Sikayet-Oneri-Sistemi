# Generated by Django 4.1.1 on 2022-11-27 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=120, verbose_name='Başlık')),
                ('sikayet', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('sikayetciMail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Mail Adresi(İsteğe Bağlı)')),
                ('sikayetTarihi', models.DateTimeField()),
                ('mesajTuru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mesaj.tur', verbose_name='Tür(Zorunlu)')),
            ],
        ),
    ]
