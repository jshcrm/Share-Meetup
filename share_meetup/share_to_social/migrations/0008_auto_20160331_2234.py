# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 22:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share_to_social', '0007_meetup_event_photo_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitter_profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Twitter_Profile',
        ),
    ]
