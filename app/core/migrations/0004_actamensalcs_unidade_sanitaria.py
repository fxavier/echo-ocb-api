# Generated by Django 3.1.5 on 2021-01-22 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210122_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='actamensalcs',
            name='unidade_sanitaria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.unidadesanitaria'),
            preserve_default=False,
        ),
    ]
