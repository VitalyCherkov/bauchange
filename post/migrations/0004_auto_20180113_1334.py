# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-13 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_about'),
        ('post', '0003_auto_20180106_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(choices=[(-1, 'Dislike'), (1, 'Like')])),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='own_posts', to='userprofile.UserProfile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AddField(
            model_name='likedislike',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
        migrations.AddField(
            model_name='likedislike',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.UserProfile'),
        ),
        migrations.AddField(
            model_name='post',
            name='like_dislike',
            field=models.ManyToManyField(through='post.LikeDislike', to='userprofile.UserProfile'),
        ),
    ]