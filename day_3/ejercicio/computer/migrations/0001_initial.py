# Generated by Django 4.0.6 on 2022-07-20 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contadorComputadoras', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DispositivoDeEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDeEntrada', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('contadorMonitor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Raton',
            fields=[
                ('dispositivodeentrada_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='computer.dispositivodeentrada')),
                ('contadorRatones', models.IntegerField()),
            ],
            bases=('computer.dispositivodeentrada',),
        ),
        migrations.CreateModel(
            name='Teclado',
            fields=[
                ('dispositivodeentrada_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='computer.dispositivodeentrada')),
                ('contadorTeclados', models.IntegerField()),
            ],
            bases=('computer.dispositivodeentrada',),
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contadorOrdenes', models.IntegerField()),
                ('computadoras', models.ManyToManyField(to='computer.computadora')),
            ],
        ),
        migrations.AddField(
            model_name='computadora',
            name='monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer.monitor'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='raton',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer.raton'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='teclado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer.teclado'),
        ),
    ]
