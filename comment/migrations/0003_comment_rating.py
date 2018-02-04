# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-14 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_about'),
        ('comment', '0002_remove_comment_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.ManyToManyField(related_name='liked_comments', to='userprofile.UserProfile'),
        ),
    ]