# Generated by Django 2.2.4 on 2020-03-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsandcommodities', '0002_auto_20200328_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='name',
            field=models.CharField(default='None', max_length=250),
            preserve_default=False,
        ),
    ]
