# Generated by Django 2.0.2 on 2018-03-07 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180307_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='SeeFirst',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='SeeFirst',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='SeeFirst',
            field=models.PositiveIntegerField(),
        ),
    ]
