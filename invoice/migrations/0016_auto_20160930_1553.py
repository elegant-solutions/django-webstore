# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0015_order_oder_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='oder_id',
            new_name='order_id',
        ),
    ]
