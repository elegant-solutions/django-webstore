# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_auto_20160919_2117'),
        ('invoice', '0007_auto_20160921_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shipping_total_price', models.DecimalField(default=5.99, max_digits=5, decimal_places=2)),
                ('order_total', models.DecimalField(max_digits=5, decimal_places=2)),
                ('billing_address', models.ForeignKey(related_name='billing_address', to='invoice.UserAddress')),
                ('cart', models.ForeignKey(to='carts.Cart')),
                ('shipping_address', models.ForeignKey(related_name='shipping_address', to='invoice.UserAddress')),
                ('user', models.ForeignKey(to='invoice.UserCheckout')),
            ],
        ),
    ]
