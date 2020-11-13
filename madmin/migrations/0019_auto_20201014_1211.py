# Generated by Django 3.1 on 2020-10-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0018_auto_20201014_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user_model',
            name='urole',
            field=models.CharField(choices=[(1, 'super admin'), (2, 'teammate'), (3, 'operator')], default=3, max_length=30),
        ),
    ]
