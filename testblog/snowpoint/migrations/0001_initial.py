# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LeagueStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('entry_type', models.CharField(choices=[('C', 'Challenger'), ('G', 'Gym Leader'), ('E', 'Elite Four')], max_length=1)),
                ('league', models.ForeignKey(to='snowpoint.League')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('outcome', models.IntegerField(choices=[(-1, 'Champion Win'), (0, 'Tie'), (1, 'Challenger Win')])),
                ('match_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(unique=True, max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='challenger',
            field=models.ForeignKey(to='snowpoint.Participant', related_name='challenger'),
        ),
        migrations.AddField(
            model_name='match',
            name='champion',
            field=models.ForeignKey(to='snowpoint.Participant', related_name='champion'),
        ),
        migrations.AddField(
            model_name='leaguestatus',
            name='participant',
            field=models.ForeignKey(to='snowpoint.Participant'),
        ),
        migrations.AddField(
            model_name='league',
            name='participants',
            field=models.ManyToManyField(through='snowpoint.LeagueStatus', to='snowpoint.Participant'),
        ),
    ]
