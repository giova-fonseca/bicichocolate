# Generated by Django 3.0.4 on 2021-07-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0012_auto_20210704_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruebafecha',
            name='year_of_validity',
            field=models.DateField(blank=True, null=True, verbose_name='Year of Validity'),
        ),
    ]
