# Generated by Django 3.0.4 on 2021-03-19 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imagen',
            field=models.ImageField(default='sitio/static/images/no-img.jpg', upload_to='gallery'),
        ),
    ]
