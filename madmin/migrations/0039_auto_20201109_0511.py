# Generated by Django 3.1 on 2020-11-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0038_bot_details_ct_clr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot_details',
            name='ct_clr',
            field=models.CharField(default='#50A59D', max_length=100, verbose_name='Color Of Bot'),
        ),
    ]
