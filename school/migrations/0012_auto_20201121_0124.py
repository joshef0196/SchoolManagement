# Generated by Django 2.0.3 on 2020-11-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20201120_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeelist',
            name='desig_name',
            field=models.CharField(choices=[('1', 'Principal'), ('2', 'Employee '), ('3', 'IT Officer'), ('4', 'Vice Principal')], max_length=1),
        ),
    ]
