# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-14 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_a', '0004_userinfo_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='IP_host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='tags',
            field=models.ManyToManyField(to='admin_a.IP_host'),
        ),
    ]