# Generated by Django 3.0.4 on 2021-07-02 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0002_auto_20210418_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('direction', models.CharField(max_length=250)),
                ('telephone', models.CharField(max_length=12)),
                ('logo', models.ImageField(blank=True, upload_to='logo')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'PointSales',
            },
        ),
        migrations.DeleteModel(
            name='POS',
        ),
        migrations.RemoveField(
            model_name='category',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='category',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='chocolatetype',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='flavor',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='flavor',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='image',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='product',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='product',
            name='nombre',
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='chocolatetype',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='flavor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
