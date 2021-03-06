# Generated by Django 3.1.5 on 2021-01-22 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210121_0928'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actamensalcg',
            options={'verbose_name': 'Acta Mensal do CG', 'verbose_name_plural': 'Actas Mensais do CG'},
        ),
        migrations.AlterModelOptions(
            name='actamensalcs',
            options={'verbose_name': 'Acta Mensal do CS', 'verbose_name_plural': 'Actas Mensais do CS'},
        ),
        migrations.AlterModelOptions(
            name='dialogocomunitario',
            options={'verbose_name': 'Dialogo Comunitario', 'verbose_name_plural': 'Dialogos Comunitarios'},
        ),
        migrations.AlterModelOptions(
            name='programaradio',
            options={'verbose_name': 'Programa da Radio', 'verbose_name_plural': 'Programas da Radio'},
        ),
        migrations.AlterModelOptions(
            name='resumomensalvsl',
            options={'verbose_name': 'Resumo Mensal de VSL', 'verbose_name_plural': 'Resumos Mensais de VSL'},
        ),
        migrations.AlterModelOptions(
            name='unidadesanitaria',
            options={'verbose_name': 'Unidade Sanitaria', 'verbose_name_plural': 'Unidades Sanitarias'},
        ),
        migrations.AddField(
            model_name='programaradio',
            name='unidade_sanitaria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.unidadesanitaria'),
            preserve_default=False,
        ),
    ]
