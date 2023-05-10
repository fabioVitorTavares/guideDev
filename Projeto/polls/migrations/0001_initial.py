# Generated by Django 4.2.1 on 2023-05-10 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('total_contribuicoes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
                ('resumo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=500)),
                ('codigo', models.CharField(max_length=500)),
                ('total_likes', models.IntegerField(default=0)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.autor')),
                ('tecnologia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.tecnologia')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=200)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.autor')),
                ('tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.tutorial')),
            ],
        ),
    ]
