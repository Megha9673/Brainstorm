# Generated by Django 2.0 on 2018-01-04 23:04

import brainstorm.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainstorm', '0003_level_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='ans',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='person',
            name='phoneno',
            field=models.IntegerField(validators=[brainstorm.models.validate_even]),
        ),
    ]
