# Generated by Django 2.0.3 on 2020-11-20 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_auto_20201121_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeelist',
            name='national_id',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='employeelist',
            name='starting_salary',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
