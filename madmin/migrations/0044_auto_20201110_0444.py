# Generated by Django 3.1 on 2020-11-10 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0043_auto_20201109_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_configuration',
            name='bnk_dbrd_urls',
            field=models.URLField(blank=True, default='example.com', max_length=100, null=True, verbose_name='Bank Dashboard Urls'),
        ),
    ]
