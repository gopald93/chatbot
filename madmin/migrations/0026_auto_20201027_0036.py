# Generated by Django 3.1 on 2020-10-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0025_auto_20201026_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='default_image_icon_gallery',
            name='image_path',
            field=models.ImageField(unique=True, upload_to='images/'),
        ),
    ]
