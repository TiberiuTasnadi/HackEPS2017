# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_auto_20171118_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qwe', to='crawler.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='crawler.User')),
            ],
        ),
    ]
