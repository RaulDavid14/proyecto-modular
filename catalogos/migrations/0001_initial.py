# Generated by Django 5.1.1 on 2024-10-20 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatEstadoCivil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_largo', models.CharField(max_length=30, verbose_name='Nombre Largo')),
                ('abreviacion', models.CharField(max_length=5, verbose_name='Nombre Corto')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Estado cívil',
                'verbose_name_plural': 'Estados Civiles',
                'db_table': 'catalogo_estado_civil',
            },
        ),
        migrations.CreateModel(
            name='CatNivelEducativo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_largo', models.CharField(max_length=30, verbose_name='Nombre Largo')),
                ('abreviacion', models.CharField(max_length=5, verbose_name='Nombre Corto')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Nivel educativo',
                'verbose_name_plural': 'Niveles educativos',
                'db_table': 'catalogo_nivel_educativo',
            },
        ),
        migrations.CreateModel(
            name='CatPoblacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_largo', models.CharField(max_length=30, verbose_name='Nombre Largo')),
                ('abreviacion', models.CharField(max_length=5, verbose_name='Nombre Corto')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Población',
                'verbose_name_plural': 'Tipos de Población',
                'db_table': 'catalogo_poblacion',
            },
        ),
        migrations.CreateModel(
            name='CatSexo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_largo', models.CharField(max_length=30, verbose_name='Nombre Largo')),
                ('abreviacion', models.CharField(max_length=5, verbose_name='Nombre Corto')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Sexo',
                'verbose_name_plural': 'Sexos',
                'db_table': 'catalogo_sexo',
            },
        ),
    ]