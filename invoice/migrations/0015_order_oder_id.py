# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0014_auto_20160929_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='oder_id',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
