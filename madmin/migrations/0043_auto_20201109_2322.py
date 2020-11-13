# Generated by Django 3.1 on 2020-11-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0042_auto_20201109_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_configuration',
            name='bnk_dbrd_urls',
            field=models.URLField(default='dashboard/example.com', max_length=100, verbose_name='Bank Dashboard Urls'),
        ),
        migrations.AlterField(
            model_name='bank_configuration',
            name='bnk_name',
            field=models.CharField(default='example', max_length=50, verbose_name='Bank Name'),
        ),
        migrations.AlterField(
            model_name='bank_configuration',
            name='bnk_urls',
            field=models.URLField(default='example.com', max_length=100, verbose_name='Bank Urls'),
        ),
        migrations.AlterField(
            model_name='bank_configuration',
            name='max_act_user',
            field=models.IntegerField(default=1, verbose_name='Maximum Activate User Allow'),
        ),
    ]