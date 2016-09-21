# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_auto_20160921_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=120, choices=[(b'billing', b'Billing'), (b'shipping', b'Shipping')])),
                ('street', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('zipcode', models.IntegerField(max_length=120)),
                ('user', models.ForeignKey(to='invoice.UserCheckout')),
            ],
        ),
    ]
