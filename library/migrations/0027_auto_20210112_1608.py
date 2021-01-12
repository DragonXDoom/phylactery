# Generated by Django 3.1.4 on 2021-01-12 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('library', '0026_tagparent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagparent',
            name='child_tag',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='taggit.tag'),
        ),
    ]
