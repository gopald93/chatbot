# Generated by Django 3.1 on 2020-10-27 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0023_auto_20201020_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Default_Image_Icon_Gallery',
            fields=[
                ('image_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('image_path', models.ImageField(unique=True, upload_to='images/')),
            ],
        ),
    ]
