# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0011_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercheckout',
            name='braintree_id',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
