# Generated by Django 4.2.1 on 2023-05-23 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_tutorialconteudo_tutorial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='codigo',
            options={'verbose_name_plural': 'Códigos'},
        ),
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name_plural': 'Comentários'},
        ),
        migrations.AlterModelOptions(
            name='marcacao',
            options={'verbose_name_plural': 'Marcações'},
        ),
        migrations.AlterModelOptions(
            name='tecnologia',
            options={'verbose_name_plural': 'Tecnologias'},
        ),
        migrations.AlterModelOptions(
            name='tutorial',
            options={'verbose_name_plural': 'Tutoriais'},
        ),
        migrations.AlterModelOptions(
            name='tutorialconteudo',
            options={'ordering': ['tutorial', 'ordem'], 'verbose_name_plural': 'Conteúdos dos Tutoriais'},
        ),
        migrations.AlterField(
            model_name='tutorialconteudo',
            name='ordem',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
