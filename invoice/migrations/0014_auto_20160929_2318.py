# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0013_auto_20160929_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'created', max_length=120, choices=[(b'created', b'Created'), (b'paid', b'Paid'), (b'shipped', b'Shipped'), (b'refunded', b'Refunded')]),
        ),
    ]
