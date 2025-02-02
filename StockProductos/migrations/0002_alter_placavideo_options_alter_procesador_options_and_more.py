# Generated by Django 5.0.3 on 2024-03-21 12:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockProductos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placavideo',
            options={'ordering': ['precio'], 'verbose_name': 'Placa de video', 'verbose_name_plural': 'Placas de video'},
        ),
        migrations.AlterModelOptions(
            name='procesador',
            options={'ordering': ['precio'], 'verbose_name': 'Procesador', 'verbose_name_plural': 'Procesadores'},
        ),
        migrations.AlterModelOptions(
            name='teclado',
            options={'ordering': ['precio']},
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
