# Generated by Django 4.2.2 on 2023-06-11 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appsocio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lectura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anterior', models.FloatField()),
                ('actual', models.FloatField()),
                ('consumo', models.FloatField()),
                ('pagoconsumo', models.FloatField()),
                ('multa', models.FloatField()),
                ('pagototal', models.FloatField()),
                ('mes', models.CharField(choices=[('ENERO', 'ENERO'), ('FEBRERO', 'FEBRERO'), ('MARZO', 'MARZO'), ('ABRIL', 'ABRIL'), ('MAYO', 'MAYO'), ('JUNIO', 'JUNIO'), ('JULIO', 'JULIO'), ('AGOSTO', 'AGOSTO'), ('SEPTIEMBRE', 'SEPTIEMBRE'), ('OCTUBRE', 'OCTUBRE'), ('NOVIEMBRE', 'NOVIEMBRE'), ('DICIEMBRE', 'DICIEMBRE')], max_length=10)),
                ('anio', models.IntegerField(choices=[(2022, 2022), (2023, 2023), (2024, 2024)])),
                ('estado', models.BooleanField()),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='appsocio.socio')),
            ],
            options={
                'db_table': 'lectura',
                'managed': True,
            },
        ),
    ]
