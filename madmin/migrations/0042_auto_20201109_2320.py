# Generated by Django 3.1 on 2020-11-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0041_auto_20201109_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_configuration',
            name='bnk_name',
            field=models.CharField(blank=True, default='example', max_length=50, null=True, verbose_name='Bank Name'),
        ),
        migrations.AlterField(
            model_name='bank_configuration',
            name='bnk_urls',
            field=models.URLField(blank=True, default='example.com', max_length=100, null=True, verbose_name='Bank Urls'),
        ),
        migrations.AlterField(
            model_name='bank_configuration',
            name='max_act_user',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Maximum Activate User Allow'),
        ),
    ]