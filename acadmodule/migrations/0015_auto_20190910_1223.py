# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-10 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acadmodule', '0014_auto_20190910_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculumcourse',
            name='course_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='curriculumcourse',
            name='course_type',
            field=models.CharField(blank=True, choices=[('Core', 'Professional Core'), ('Elective', 'Professional Elective'), ('Lab', 'Professional Lab'), ('Project', 'Professional Project'), ('ES', 'Engineering Science'), ('NS', 'Natural Science'), ('HS', 'Humanities'), ('DS', 'Design'), ('MN', 'Manufacturing'), ('MS', 'Management Science')], max_length=200, null=True),
        ),
    ]