# Generated by Django 3.1.4 on 2021-01-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_auto_20210107_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowrecord',
            name='date_returned',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
