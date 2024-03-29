# Generated by Django 2.2 on 2019-04-16 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_auto_20190416_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workers',
            name='country',
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_country', to='workers.Country'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers_city', to='workers.City'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers_position', to='workers.Position'),
        ),
    ]
