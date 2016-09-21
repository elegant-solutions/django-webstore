# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_auto_20160921_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercheckout',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
