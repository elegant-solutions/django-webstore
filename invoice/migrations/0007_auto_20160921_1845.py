# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_auto_20160921_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='zipcode',
            field=models.CharField(max_length=10),
        ),
    ]
