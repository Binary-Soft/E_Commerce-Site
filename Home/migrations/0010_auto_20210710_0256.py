# Generated by Django 3.2.4 on 2021-07-09 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_auto_20210710_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pic2',
            field=models.ImageField(default=None, upload_to='picture/'),
        ),
        migrations.AddField(
            model_name='product',
            name='pic3',
            field=models.ImageField(default=None, upload_to='picture/'),
        ),
        migrations.AddField(
            model_name='product',
            name='pic4',
            field=models.ImageField(default=None, upload_to='picture/'),
        ),
    ]
