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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('entry_type', models.CharField(max_length=1, choices=[('C', 'Challenger'), ('G', 'Gym Leader'), ('E', 'Elite Four')])),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('outcome', models.IntegerField(choices=[(-1, 'Champion Win'), (0, 'Tie'), (1, 'Challenger Win')])),
                ('match_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='challenger',
            field=models.ForeignKey(related_name='challenger', to='snowpoint.Participant'),
        ),
        migrations.AddField(
            model_name='match',
            name='champion',
            field=models.ForeignKey(related_name='champion', to='snowpoint.Participant'),
        ),
        migrations.AddField(
            model_name='league',
            name='participants',
            field=models.ManyToManyField(to='snowpoint.Participant'),
        ),
    ]
