# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_cart_tax_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='tax_percentage',
            field=models.DecimalField(default=Decimal('0.089'), max_digits=10, decimal_places=5),
        ),
    ]
