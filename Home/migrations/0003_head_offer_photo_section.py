# Generated by Django 3.2.4 on 2021-07-07 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20210706_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Head_Offer_Photo_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notice', models.CharField(max_length=500)),
                ('picture', models.ImageField(upload_to='HeadOfferPhotoSection/')),
            ],
        ),
    ]
