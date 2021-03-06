# Generated by Django 2.0.2 on 2018-03-06 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180305_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Brands', to='home.Category')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='Brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='home.Brand'),
            preserve_default=False,
        ),
    ]
