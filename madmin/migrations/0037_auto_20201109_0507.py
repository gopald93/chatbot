# Generated by Django 3.1 on 2020-11-09 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0036_auto_20201029_0517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot_details',
            name='ct_clr',
        ),
        migrations.RemoveField(
            model_name='bot_details',
            name='sw_wlcmsg',
        ),
        migrations.RemoveField(
            model_name='bot_details',
            name='wm_dflt_lan',
        ),
        migrations.RemoveField(
            model_name='bot_details',
            name='wm_dflt_wlcmsg',
        ),
    ]