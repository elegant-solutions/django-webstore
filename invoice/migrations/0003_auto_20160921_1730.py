# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20160921_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercheckout',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
