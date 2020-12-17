# Generated by Django 3.0.6 on 2020-12-16 21:49

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='language',
        ),
        migrations.RemoveField(
            model_name='keyword',
            name='ngram',
        ),
        migrations.RemoveField(
            model_name='keyword',
            name='number',
        ),
        migrations.AddField(
            model_name='keyword',
            name='settings',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]