# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-29 12:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_remove_post_like_dislike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likedislike',
            name='post',
        ),
        migrations.RemoveField(
            model_name='likedislike',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='LikeDislike',
        ),
    ]
