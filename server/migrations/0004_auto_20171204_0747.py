# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20171108_0623'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('macAddress', models.TextField()),
                ('rootUrl', models.TextField()),
                ('urlTag', models.TextField()),
                ('pageTitle', models.TextField()),
                ('pageClass', models.TextField()),
                ('objClass', models.TextField()),
                ('objTagClass', models.TextField()),
                ('filter', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='guitarsheet',
            name='link',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='guitarsheet',
            name='title',
            field=models.TextField(),
        ),
    ]
