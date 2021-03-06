# Generated by Django 3.1.5 on 2021-01-26 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210125_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='actamensalcg',
            name='distrito',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.distrito'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actamensalcg',
            name='provincia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.provincia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actamensalcs',
            name='distrito',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.distrito'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actamensalcs',
            name='provincia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.provincia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dialogocomunitario',
            name='distrito',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.distrito'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dialogocomunitario',
            name='provincia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.provincia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programaradio',
            name='distrito',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.distrito'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programaradio',
            name='provincia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.provincia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resumomensalvsl',
            name='distrito',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.distrito'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resumomensalvsl',
            name='provincia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.provincia'),
            preserve_default=False,
        ),
    ]
