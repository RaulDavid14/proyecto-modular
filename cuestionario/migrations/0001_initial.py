# Generated by Django 5.1.1 on 2024-10-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='Pregunta')),
                ('sig_pregunta', models.IntegerField(verbose_name='siguiente pregunta')),
                ('tipo_respuesta', models.IntegerField(verbose_name='tipo de preguntas')),
            ],
        ),
    ]