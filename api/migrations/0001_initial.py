# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spirit', '0007_auto_20150711_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomCategory',
            fields=[
                ('category_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='spirit.Category')),
                ('image', models.ImageField(upload_to=b'')),
            ],
            options={
            },
            bases=('spirit.category',),
        ),
    ]
